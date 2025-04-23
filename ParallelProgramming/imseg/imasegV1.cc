//#include <iostream>
#include <x86intrin.h>
#include <omp.h>
#include "is.h"
#include <vector>
#include "vector.h"
#include <sys/time.h>

/*
constexpr float4_t float4_I={1,0,0,0};
constexpr float4_t float4_J={0,1,0,0};
constexpr float4_t float4_IJ={1,1,0,0};
constexpr float4_t float4_KL={0,0,1,1};
*/
constexpr float4_t float4_1={1,1,1,1};


static double get_time() {
    struct timeval tm;
    gettimeofday(&tm, NULL);
    return static_cast<double>(tm.tv_sec)
           + static_cast<double>(tm.tv_usec) / 1E6;
}

Result segment(int ny, int nx, const float* data) {

    std::vector<float> vd(nx*ny);
    for (int i=0;i<nx*ny;i++) {
        for (int j=0;j<3;j++) {
            vd[i]=data[3*i];
        }
    }

    //basic blocks ("corners")
    float4_t *ss=float4_alloc((nx+1)*(ny+1));
    for (int i=0;i<=nx;i++) ss[i]=float4_0;//Empty first row
    const int NX=nx+1;
	bool flag = nx==ny && nx>=10;

    for(int y1=1;y1<=ny;y1++) {
        ss[y1*NX]=float4_0;//empty first elem

        for(int x1=1;x1<=nx;x1++) {
            float4_t tmp = float4_1*vd[(y1-1)*nx+x1-1];
            tmp -= ss[(y1-1)*NX+x1-1];
            tmp += ss[(y1-1)*NX+x1];
            tmp += ss[y1*NX+x1-1];
            ss[y1*NX+x1] = tmp;
        }
    }

	if(flag) {
		for(int y1=1;y1<=ny;y1++)
	        for(int x1=1;x1<=nx;x1++)
    	        //put mirror images across diagonal
        	ss[y1 * NX + x1][1] = ss[x1 * NX + y1][0];

	}

    int glob_size=0;
    float glob_max=0.0;
    int all=nx*ny+nx+ny+1;
    int z=nx*ny;

    //some pre-computed values for the inner-most loop
    const float vz=ss[all-1][0];
    const float vzz=vz*vz;
    const float vz2 = 2*vz;

    //The main loop
#pragma omp parallel
    {
#pragma omp for schedule(dynamic,4)
        for (int size=1;size<z;size++) {
	    const float xi = 1.0/size;
            const float yi = 1.0/(z-size);
            const float xiyi = xi + yi;
            const float yivzz = yi*vzz;
            const float yivz2 = yi*vz2;
			float loc_max=0.0f;

            for (int w=nx;w>0;w--) {
                while(size%w) w--;//continue;
                int h=size/w;

                for (int y0=0;y0<=ny-h;y0++) {
                    int y1_NX=NX*(y0+h);
                    int y0_NX=y0*NX;
                    int lim = flag? y0:0;

                    for (int x0=lim;x0<=nx-w;x0++) {
                        float4_t vx = ss[y1_NX+x0+w]+ss[y0_NX+x0];
			vx -= ss[y1_NX+x0]+ss[y0_NX+x0+w];
			float4_t vxx = vx*(xiyi*vx-yivz2)+yivzz;
			//this is useless for non-square images, but cleaner
			// than using upper level condition - benchmark is for squared,
			// and for non-squared just one max op would suffice.
			float new_max = std::max(vxx[0],vxx[1]);
                        loc_max = std::max(loc_max, new_max);
                    }
                }
            }
	#pragma omp critical
            {
                if(loc_max>glob_max) {
                    glob_max=loc_max;
                    glob_size=size;
                } //else loc_max=glob_max;
            }
        }
    }
    //Search the specific window of given size
    Result result;
    int size=glob_size;
    const float xi = 1.0/size;
    const float yi = 1.0/(z-size);
    const float xiyi = xi + yi;
    const float yivzz = yi*vzz;
    const float yivz2 = yi*vz2;

    for (int w=nx;w>0;w--) {
        while(size%w) w--;
        int h=size/w;

        for (int y0=0;y0<=ny-h;y0++) {
            int y1_NX=NX*(y0+h);
            int y0_NX=y0*NX;

            for (int x0=0;x0<=nx-w;x0++) {
                const float4_t vx = ss[y1_NX+x0+w] + ss[y0_NX+x0] - ss[y1_NX+x0] - ss[y0_NX+x0+w];
                const float4_t new_max = vx*(xiyi*vx-yivz2)+yivzz;

                if(new_max[0]>=glob_max) {

                    int X0=x0;
                    int X1=x0+w;
                    int Y0=y0;
                    int Y1=y0+h;

                    float4_t inner = float4_1*(ss[(1+nx)*Y1+X1][0] + ss[(1+nx)*Y0+X0][0] -
                                               ss[(1+nx)*Y1+X0][0] - ss[(1+nx)*Y0+X1][0]);
                    float4_t outer= vz-inner;
                    int x=(Y1-Y0)*(X1-X0);
                    int y=z-x;
                    float dx= x==0 ? 0 :1.0/x;
                    float dy= y==0 ? 0 :1.0/y;
                    inner*=dx;
                    outer*=dy;

                    result = Result { Y0, X0, Y1, X1,{(float)outer[0],(float)outer[1],(float)outer[2]}, {(float)inner[0],(float)inner[1],(float)inner[2]} };

                }
            }
        }
    }

    std::free(ss);
    return result;
}


