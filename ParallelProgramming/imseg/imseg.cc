#include <iostream>
#include <omp.h>
#include "is.h"
#include "vector.h"
#include <sys/time.h>

/*
static double get_time() {
    struct timeval tm;
    gettimeofday(&tm, NULL);
    return static_cast<double>(tm.tv_sec)
        + static_cast<double>(tm.tv_usec) / 1E6;
}
*/

Result segment(int ny, int nx, const float* data) {

	double4_t *vd=double4_alloc(nx*ny);
	for (int i=0;i<nx*ny;i++) {
		for (int j=0;j<3;j++) {
			vd[i][j]=data[3*i+j];
		}
	}

	double4_t *ss=double4_alloc((nx+1)*(ny+1));
	for (int i=0;i<=nx;i++) ss[i]=double4_0;//Empty first row
	const int NX=nx+1;

	for(int y1=1;y1<=ny;y1++) {
		ss[y1*NX]=double4_0;//empty first elem
		for(int x1=1;x1<=nx;x1++) {
			double4_t tmp = vd[(y1-1)*nx+x1-1];
			tmp -= ss[(y1-1)*NX+x1-1];
			tmp += ss[(y1-1)*NX+x1];
			tmp += ss[y1*NX+x1-1];
			ss[y1*NX+x1] = tmp;
		}
	}

	double glob_max=0.0;
	int glob_size=0;
	int all=nx*ny+nx+ny+1;
	int z=nx*ny;

	//some pre-computed values for the inner-most loop
	const double4_t vz=ss[all-1];
	const double4_t vzz=vz*vz;
	const double4_t vz2 = 2*vz;

	//The main loop
#pragma omp parallel
{
	#pragma omp for schedule(dynamic,8)
	for (int size=z-1;size>0;size--) {
		double xi = 1.0/size;
		double yi = 1.0/(z-size);
		double xiyi = xi + yi;
		double4_t yivzz = yi*vzz;
		double4_t yivz2 = yi*vz2;
		int lim = size < nx ? size : nx;
    	double loc_max=0.0;

		for (int w=lim;w>0;w--) {
			while(size%w) w--;//continue;
			int h=size/w;

			for (int y0=0;y0<=ny-h;y0++) {
				int y1_NX=NX*(y0+h);
				int y0_NX=y0*NX;

				for (int x0=0;x0<=nx-w;x0++) {

					__builtin_prefetch(&ss[y1_NX+x0+w+4]);
	                __builtin_prefetch(&ss[y0_NX+x0+w+4]);
					__builtin_prefetch(&ss[y1_NX+x0+4]);
                    __builtin_prefetch(&ss[y0_NX+x0+4]);

					double4_t vx = ss[y1_NX+x0+w] + ss[y0_NX+x0] - ss[y1_NX+x0] - ss[y0_NX+x0+w];
					double4_t vxx = vx*(xiyi*vx-yivz2)+yivzz;
					double new_max = vxx[0]+vxx[1]+vxx[2];
					if(new_max>loc_max) loc_max=new_max;
				}
			}
		}

		#pragma omp critical
		{
			if(loc_max>glob_max) {
				glob_max=loc_max;
				glob_size=size;
			} else loc_max=glob_max;
		}
	}
}
	Result result;//{0,0,0,0,{0,0,0},{0,0,0}};
	int size = glob_size;
	double xi = 1.0/size;
    double yi = 1.0/(z-size);
    double xiyi = xi + yi;
    double4_t yivzz = yi*vzz;
    double4_t yivz2 = yi*vz2;

//#pragma omp parallel for
	for (int w=nx;w>0;w--) {
            if(size%w) continue;
            int h=size/w;

            for (int y0=0;y0<=ny-h;y0++) {
                int y1_NX=NX*(y0+h);
                int y0_NX=y0*NX;

                for (int x0=0;x0<=nx-w;x0++) {
                    double4_t vx = ss[y1_NX+x0+w] + ss[y0_NX+x0] - ss[y1_NX+x0] - ss[y0_NX+x0+w];
                    double4_t vxx = vx*(xiyi*vx-yivz2)+yivzz;
                    double new_max = vxx[0]+vxx[1]+vxx[2];

                    if(new_max>=glob_max) {

						int X0=x0;int X1=x0+w;int Y0=y0;int Y1=y0+h;

					    double4_t inner=ss[(1+nx)*Y1+X1] + ss[(1+nx)*Y0+X0] - ss[(1+nx)*Y1+X0] - ss[(1+nx)*Y0+X1];
					    double4_t outer= vz-inner;
    					int x=(Y1-Y0)*(X1-X0);
    					int y=z-x;
    					double dx= x==0 ? 0 :1.0/x;
    					double dy= y==0 ? 0 :1.0/y;
    					inner*=dx;
    					outer*=dy;

						//This is an ugly way to exit... but it gives a couple of .01's of
						result = Result  { Y0, X0, Y1, X1,{(float)outer[0],(float)outer[1],(float)outer[2]}, {(float)inner[0],(float)inner[1],(float)inner[2]} };
    					std::free(ss);std::free(vd);
    					return result;

                    }
                }
            }
        }

	std::free(ss);std::free(vd);
    return result;

}


