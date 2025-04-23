
#include "cp.h"
#include <math.h>
#include <stdlib.h>
#include "vector.h"
#include <vector>

void correlate(int ny, int nx, const float* data, float* result) {
    
    double s,ss;
    double modes[ny];
    // elements per vector
    constexpr int nb = 4;
    // vectors per input row
    int na = (nx + nb - 1) / nb;
    double4_t *vd = double4_alloc(ny*na);
    int nxx = 4*na;
    std::vector<double> cpy(nxx*ny,0.0d);

    double inx = 1.0d/nx;

    for (int row=0;row<ny;row++) {
	s=0.0d;
	for (int col=0;col<nx;col++) {
	    s += data[nx*row+col];
	}
	ss=0.0d;
	s*=inx;
	for (int col=0;col<nx;col++) {
	    double elem = data[nx*row+col]-s;
	    cpy[nxx*row + col] = elem;
	    ss += pow(elem,2);
	}
		//ss = 1.0d/sqrt(ss);
	modes[row]=1.0/sqrt(ss);

	for (int vecs = 0; vecs < na; vecs++) {
	    for (int elem = 0; elem < nb; elem++) {
	        vd[na * row + vecs][elem] = cpy[nxx * row + vecs * nb + elem];
	    }
	}

    }

    for (int row_1=0;row_1<ny;row_1++) {
	for (int row_2=row_1;row_2<ny;row_2++) {
	    double4_t cumsum = {0.0d,0.0d,0.0d,0.0d};
	    for (int col=0;col<na;col++) {
		cumsum += vd[na*row_1+col]*vd[na*row_2+col];//(temp[src_row_1*nx+col])*(temp[src_row_2*nx+col]);
	    }
	    result[row_2+ny*row_1]=modes[row_1]*modes[row_2]*(cumsum[0]+cumsum[1]+cumsum[2]+cumsum[3]);
    	}
    }
    std::free(vd);
}

