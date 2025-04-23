#include "is.h"
#include <math.h>
#include <cstdlib>
#include <iostream>
#include <cuda_runtime.h>
#include <stdlib.h>
#include <sys/time.h>

inline void check(cudaError_t err, const char* context) {
    if (err != cudaSuccess) {
        std::cerr << "CUDA error: " << context << ": "<< cudaGetErrorString(err) << std::endl;
        std::exit(EXIT_FAILURE);
    }
}
#define CHECK(x) check(x, #x)

int static divup(int a, int b) {
    return (a + b - 1)/b;
}

__global__ void window_kernel(const float *ss, int *utils, const float vz, const int ny, const int nx) {

	int w = threadIdx.x + blockIdx.x*blockDim.x+1;
	int h = threadIdx.y + blockIdx.y*blockDim.y+1;
	int size = w*h;
	int z = nx*ny;
	
	//if(w>nx || h>ny) return;
	
	float xi = 1.0/size;
	float yi = 1.0/(z - size);
	float xiyi = xi + yi;
	float yivzz = yi*vz*vz;
	float yivz2 = yi*vz*2;
	int NX = nx + 1;
	float loc_max = 0.0f;

	for (int y0=0;y0<ny-h+1;y0++) {
		int y1_NX=NX*(y0+h);
        int y0_NX=y0*NX;

		#pragma unroll
		for (int x0=0;x0<nx-w+1;x0++) {
			float vx = ss[y1_NX+x0+w]+ss[y0_NX+x0] - ss[y1_NX+x0] - ss[y0_NX+x0+w];
			float vxx = (xiyi*vx-yivz2);//vx*(xiyi*vx-yivz2)+yivzz;
			vxx = vx*vxx + yivzz;
            loc_max = loc_max>vxx?loc_max:vxx;
        }
    }

	atomicMax(&utils[size], __float_as_int(loc_max));
}


Result segment(int ny, int nx, const float* data) {
    // FIXME
    int threadsY=8;
    int threadsX=16;

    //basic blocks ("corners")
    float *ss= new float[(nx+1)*(ny+1)];
    for (int i=0;i<=nx;i++) ss[i]=0.0f;//Empty first row
    const int NX=nx+1;

    for(int y1=1;y1<ny+1;y1++) {
        ss[y1*NX]=0.0;//empty first elem
	int i = 3*((y1-1)*nx-1);

        for(int x1=1;x1<nx+1;x1++) {
	    float tmp = data[3*x1+i];
            //float tmp = vd[(y1-1)*nx+x1-1];
            tmp -= ss[(y1-1)*NX+x1-1];
            tmp += ss[(y1-1)*NX+x1];
            tmp += ss[y1*NX+x1-1];
            ss[y1*NX+x1] = tmp;
        }
    }

    int all=nx*ny+nx+ny+1;
    int z=nx*ny;

    const float vz=ss[all-1];

    float *dGPU = NULL;
    CHECK(cudaMalloc((void**)&dGPU, all * sizeof(float)));
    CHECK(cudaMemcpy(dGPU, ss, all * sizeof(float), cudaMemcpyHostToDevice));

	//Just to be sure, initialize the utils array
    int *init = new int[z];
    for (int i=0;i<z;i++) init[i]=0;
    int *rGPU = NULL;
    CHECK(cudaMalloc((void**)&rGPU, z * sizeof(int)));
    CHECK(cudaMemcpy(rGPU, init, z * sizeof(int), cudaMemcpyHostToDevice));


    dim3 dimBlock(threadsX, threadsY);
    dim3 dimGrid(divup(nx,threadsX), divup(ny, threadsY));

    window_kernel<<<dimGrid, dimBlock>>>(dGPU, rGPU, vz, ny, nx);
    CHECK(cudaGetLastError());

    float *loc_max = new float[z];
    CHECK(cudaMemcpy(loc_max, rGPU, z * sizeof(float), cudaMemcpyDeviceToHost));
    CHECK(cudaFree(dGPU));
    CHECK(cudaFree(rGPU));

	//Poll the global maximum, and corresponding window
    float glob_max=0.0f;
    int glob_size=0;
    for(int i=1;i<z;i++) {
		if(loc_max[i]>glob_max) {
		    glob_max=loc_max[i];
			glob_size=i;
		}
    }

    //Search the specific window of given size
    Result result;
    int size=glob_size;
    const float xi = 1.0/size;
    const float yi = 1.0/(z-size);
    const float xiyi = xi + yi;
    const float yivzz = yi*vz*vz;
    const float yivz2 = yi*vz*2;

    for (int w=nx;w>0;w--) {
	while(size%w) w--;
        int h=size/w;

        for (int y0=ny-h;y0>-1;y0--) {
            int y1_NX=NX*(y0+h);
            int y0_NX=y0*NX;

            for (int x0=nx-w;x0>-1;x0--) {
                float vx = ss[y1_NX+x0+w] + ss[y0_NX+x0];
				vx -= (ss[y1_NX+x0] + ss[y0_NX+x0+w]);
                float new_max = vx*(xiyi*vx-yivz2)+yivzz;

				//exit directly from here
                if(new_max>=glob_max) {

                    int X0=x0;
                    int X1=x0+w;
                    int Y0=y0;
                    int Y1=y0+h;

                    float inner = (ss[NX*Y1+X1] + ss[NX*Y0+X0] -
                                               ss[NX*Y1+X0] - ss[NX*Y0+X1]);
                    float outer = vz-inner;
                    int x=(Y1-Y0)*(X1-X0);
                    int y=z-x;
                    float dx= x==0 ? 0 :1.0/x;
                    float dy= y==0 ? 0 :1.0/y;
                    inner*=dx;
                    outer*=dy;

                    result = Result { Y0, X0, Y1, X1,{outer,outer,outer}, {inner,inner,inner} };
		    		delete [] loc_max;
		    		delete [] ss;
					delete [] init;
		    		return result;//ugly exit, saves little time

                }
            }
        }
    }

    delete [] loc_max;
    delete [] ss;
    delete [] init;
    return result;
}


