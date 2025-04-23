#include "mf.h"
#include <vector>
#include <algorithm>
#include <omp.h>

void mf(int ny, int nx, int hy, int hx, const float* in, float* out) {

    int window=(2*hx+1)*(2*hy+1);
    //std::vector<double> v(window);// window
    std::vector<int> boundsY{0,hy,ny-hy,ny,hy,ny-hy,hy,ny-hy};
    std::vector<int> boundsX{0,nx,0,nx,0,hx,nx-hx,nx};

    if (nx>hx && ny>hy) {
        //INTERNALS
#pragma omp parallel for
            for (int row = hy; row < ny - hy; row++) {
                std::vector<double> v(window);// window
                for (int col = hx; col < nx - hx; col++) {
                    int i = 0;
                    for (int inrow = row - hy; inrow <= row + hy; inrow++) {
                        for (int incol = col - hx; incol <= col + hx; incol++) {
                            v[i] = in[inrow * nx + incol];
                            i++;
                        }

                    }
                    //check if odd/even
                    std::nth_element(v.begin(), v.begin() + i / 2, v.begin() + i);
                    out[row * nx + col] = v[i / 2];
                    if (i % 2 == 0) {
                        std::nth_element(v.begin(), v.begin() + i / 2 - 1, v.begin() + i / 2);
                        out[row * nx + col] = 0.5 * (out[row * nx + col] + v[i / 2 - 1]);
                    }
                }
            }
            //BOUNDARIES
            for (int k = 0; k < 7; k += 2) {
#pragma omp parallel for schedule(dynamic)
                for (int row = boundsY[k]; row < boundsY[k + 1]; row++) {
                    int rowlower = row >= hy ? row - hy : 0;
                    int rowupper = row + hy < ny ? row + hy : ny - 1;
                    std::vector<double> vv(window);// window
                    for (int col = boundsX[k]; col < boundsX[k + 1]; col++) {
                        int i = 0;
                        int collower = col >= hx ? col - hx : 0;
                        int colupper = col + hx < nx ? col + hx : nx - 1;
                        for (int inrow = rowlower; inrow <= rowupper; inrow++) {
                            for (int incol = collower; incol <= colupper; incol++) {
                                vv[i] = in[inrow * nx + incol];
                                i++;
                            }

                        }
                        //check if odd/even
                        std::nth_element(vv.begin(), vv.begin() + i / 2, vv.begin() + i);
                        out[row * nx + col] = vv[i / 2];
                        if (i % 2 == 0) {
                            std::nth_element(vv.begin(), vv.begin() + i / 2 - 1, vv.begin() + i / 2);
                            out[row * nx + col] = 0.5 * (out[row * nx + col] + vv[i / 2 - 1]);
                        }
                    }
                }
            }
    } else {
        //std::vector<double> v(window);// window
#pragma omp parallel for
		for (int row = 0; row < ny; row++) {
			for (int col = 0; col < nx; col++) {
                int i = 0;
				std::vector<double> v(window);
                for (int inrow = row - hy; inrow <= row + hy; inrow++) {
                    for (int incol = col - hx; incol <= col + hx; incol++) {
                        if (!(incol < 0 || incol >= nx || inrow < 0 || inrow >= ny)) {
                            v[i] = in[inrow * nx + incol];
                            i++;
                        }
                    }

                }
                //check if odd/even
                std::nth_element(v.begin(), v.begin() + i / 2, v.begin() + i);
                out[row * nx + col] = v[i / 2];
                if (i % 2 == 0) {
                    std::nth_element(v.begin(), v.begin() + i / 2 - 1, v.begin() + i/2);
                    out[row * nx + col] = 0.5 * (out[row * nx + col] + v[i / 2 - 1]);
                }

            }
        }
    }
}


