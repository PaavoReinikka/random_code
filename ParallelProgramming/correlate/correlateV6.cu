#include "cp.h"
#include <math.h>
#include <cstdlib>
#include <iostream>
#include <cuda_runtime.h>
#include <stdlib.h>

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

__global__ void mykernel(float *res, float *data, int ny, int nx) {
	int row1=(blockIdx.y*blockDim.y+threadIdx.y);
	int row2=(blockIdx.x*blockDim.x+threadIdx.x);
	if (row1>row2 || row2>=ny || row1 >=ny) {return;}
	res[row1*ny+row2]=data[row1*nx]*data[row2*nx];

	for (int col=1;col<nx;col++) 
		res[row1*ny+row2]+=data[row1*nx+col]*data[row2*nx+col];
}

void correlate(int ny, int nx, const float* data, float* result) {

    int threadsY=16;
    int threadsX=16;
    float *temp = new float[ny*nx];
    
    for (int row=0;row<ny;row++) {
		float s=0.0;
		for (int col=0;col<nx;col++) {
			s=s+data[nx*row+col];
		}
		float ss=0.0;
		s/=nx;
		for (int col=0;col<nx;col++) {
			double elem = data[nx*row+col]-s;
			ss=ss+pow(elem,2);
			temp[nx*row+col]=elem;
		}
		ss=1.0/sqrt(ss);
		for (int col=0;col<nx;col++) {
			temp[nx*row+col]=ss*temp[nx*row+col];
		}
	}

	float *dGPU = NULL;
	CHECK(cudaMalloc((void**)&dGPU, ny * nx * sizeof(float)));
        float *rGPU = NULL;
        CHECK(cudaMalloc((void**)&rGPU, ny * ny * sizeof(float)));
        CHECK(cudaMemcpy(dGPU, temp, ny * nx * sizeof(float), cudaMemcpyHostToDevice));

	dim3 dimBlock(threadsY, threadsX);
	dim3 dimGrid(divup(ny,threadsX), divup(ny, threadsY));

	mykernel<<<dimGrid, dimBlock>>>(rGPU, dGPU, ny, nx);
	CHECK(cudaGetLastError());

	CHECK(cudaMemcpy(result, rGPU, ny * ny * sizeof(float), cudaMemcpyDeviceToHost));
        CHECK(cudaFree(dGPU));
        CHECK(cudaFree(rGPU));
	
	delete [] temp;
}


