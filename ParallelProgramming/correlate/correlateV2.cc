
#include "cp.h"
#include <math.h>
#include <omp.h>
#include <vector>

void correlate(int ny, int nx, const float* data, float* result) {

    std::vector<double> temp(ny*nx);
    double inx=1.0/nx;

#pragma omp parallel for
    for (int row=0;row<ny;row++) {
        double s=0.0d;
        for (int col=0;col<nx;col++) {
            s=s+data[nx*row+col];
        }
        double ss=0.0d;
        s*=inx;
        for (int col=0;col<nx;col++) {
            double elem = data[nx*row+col]-s;
            ss += pow(elem,2);
            temp[nx*row+col]=elem;
        }
		ss=1.0/sqrt(ss);
		for (int col=0;col<nx;col++) {
			temp[nx*row+col]*=ss;
		}
    }

#pragma omp parallel for schedule(dynamic,2)
    for (int row_1=0;row_1<ny;row_1++) {
        for (int row_2=row_1;row_2<ny;row_2++) {
            double cumsum=0;
            for (int col=0;col<nx;col++) {
                cumsum+=(temp[row_1*nx+col])*(temp[row_2*nx+col]);
            }
            result[row_2+ny*row_1]=cumsum;
        }
    }

}



