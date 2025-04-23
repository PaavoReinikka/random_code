
#include "cp.h"
#include <math.h>
#include <stdlib.h>
#include <vector>

void correlate(int ny, int nx, const float* data, float* result) {

    double s,ss;
    std::vector<double> temp(nx*ny);
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
			//temp[nx*row+col]=elem;
		}
		ss=1.0d/sqrt(ss);
		for (int col=0;col<nx;col++) {
			temp[nx*row+col]=ss*(data[nx*row+col]-s);
		}
	}

    double cumsum, cumsum1, cumsum2, cumsum3, cumsum4, cumsum5, cumsum6, cumsum7, cumsum8, cumsum9;
	int extra= ny%10;

	if (ny<=10) extra=ny;
	for (int row_1=0;row_1<extra;row_1++) {
		for (int row_2=row_1;row_2<ny;row_2++) {
			cumsum=0;
            for (int col=0;col<nx;col++) {
				cumsum+=(temp[row_1*nx+col])*(temp[row_2*nx+col]);
			}
			result[row_2+ny*row_1]=cumsum;
		}
	}
	if (ny!=extra) {
        for (int row_1=extra;row_1<ny;row_1+=10) {
            for (int row_2=row_1;row_2<ny;row_2++) {
                cumsum=0;
                cumsum1=0;
                cumsum2=0;
                cumsum3=0;
                cumsum4=0;
                cumsum5=0;
                cumsum6=0;
                cumsum7=0;
                cumsum8=0;
                cumsum9=0;

                for (int col=0;col<nx;col++) {
                    cumsum+=(temp[row_1*nx+col])*(temp[row_2*nx+col]);
                    cumsum1+=(temp[(row_1+1)*nx+col])*(temp[row_2*nx+col]);
                    cumsum2+=(temp[(row_1+2)*nx+col])*(temp[row_2*nx+col]);
                    cumsum3+=(temp[(row_1+3)*nx+col])*(temp[row_2*nx+col]);
                    cumsum4+=(temp[(row_1+4)*nx+col])*(temp[row_2*nx+col]);
                    cumsum5+=(temp[(row_1+5)*nx+col])*(temp[row_2*nx+col]);
                    cumsum6+=(temp[(row_1+6)*nx+col])*(temp[row_2*nx+col]);
                    cumsum7+=(temp[(row_1+7)*nx+col])*(temp[row_2*nx+col]);
                    cumsum8+=(temp[(row_1+8)*nx+col])*(temp[row_2*nx+col]);
                    cumsum9+=(temp[(row_1+9)*nx+col])*(temp[row_2*nx+col]);

                }
                result[row_2+ny*row_1]=cumsum;
                result[row_2+ny*(1+row_1)]=cumsum1;
                result[row_2+ny*(2+row_1)]=cumsum2;
                result[row_2+ny*(3+row_1)]=cumsum3;
                result[row_2+ny*(4+row_1)]=cumsum4;
                result[row_2+ny*(5+row_1)]=cumsum5;
                result[row_2+ny*(6+row_1)]=cumsum6;
                result[row_2+ny*(7+row_1)]=cumsum7;
                result[row_2+ny*(8+row_1)]=cumsum8;
                result[row_2+ny*(9+row_1)]=cumsum9;


            }
        }
	}

}



