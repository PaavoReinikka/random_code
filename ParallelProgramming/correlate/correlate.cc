#include "cp.h"
#include <math.h>
#include <vector>
void correlate(int ny, int nx, const float* data, float* result) {
    double s,ss;
    //double *temp = new double[ny*nx];
    std::vector<double> temp(ny*nx);
    std::vector<double> modes(ny);

    double inx = 1.0/nx;

    for (int row=0;row<ny;row++) {
		s=0.0d;
		for (int col=0;col<nx;col++) {
			s=s+data[nx*row+col];
		}
		ss=0.0d;
		s*=inx;
		for (int col=0;col<nx;col++) {
			double elem = data[nx*row+col]-s;
			ss=ss+pow(elem,2);
			temp[nx*row+col]=elem;
		}
		ss=1.0d/sqrt(ss);
		modes[row]=ss;
	}
	double cumsum;
	for (int row_1=0;row_1<ny;row_1++) {
		for (int row_2=row_1;row_2<ny;row_2++) {
			cumsum=0;
			for (int col=0;col<nx;col++) {
				cumsum+=(temp[row_1*nx+col])*(temp[row_2*nx+col]);
			}
			result[row_2+ny*row_1]=modes[row_1]*modes[row_2]*cumsum;
		}
	}

}


