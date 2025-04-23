#include "cp.h"
#include <math.h>
#include <stdlib.h>
#include "vector.h"
#include <omp.h>
#include <vector>

constexpr float8_t ZERO={0,0,0,0,0,0,0,0};


void correlate(int ny, int nx, const float* data, float* result) {

    // elements per vector
    constexpr int nb = 8;
    // vectors per original input row
    int na = (nx + nb - 1) / nb;
    //blocks per input row
    int n_4x4 = (nx + 8*4 - 1)/(8*4);
	// vecs per input row
    int nn = n_4x4*4;
    int extra=nx%8;
	int extra2 = ny % 4;
    float8_t *vd = float8_alloc(ny*nn);

#pragma omp parallel
{
#pragma omp for//this waits
    for (int row=0;row<ny;row++) {
        float s=0.0f;
        for (int col=0;col<nx;col++) {
            s+=data[nx*row+col];
        }
        float ss=0.0f;
        s/=nx;
        for (int col=0;col<nx;col++) {
            float elem = data[nx*row+col]-s;
            ss+=pow(elem,2);
        }
        ss=1.0f/sqrt(ss);
        for (int vecs=0;vecs<na-1;vecs++) {
            for (int elem=0;elem<nb;elem++) {
                vd[nn*row+vecs][elem]=ss*(data[nx*row+vecs*nb+elem]-s);
            }
        }
        if (extra==0) {
            for (int i=0;i<8;i++) {
                vd[nn*row+na-1][i]=ss*(data[nx*row+(na-1)*nb+i]-s);
            }
        } else {
            for (int i=0;i<extra;i++) {
                vd[nn*row+na-1][i]=ss*(data[nx*row+(na-1)*nb+i]-s);
            }
            for (int i=extra;i<8;i++) {
                vd[nn*row+na-1][i]=0.0f;
            }
        }
        for (int vecs=na;vecs<nn;vecs++) {
            vd[nn*row+vecs]=ZERO;
        }
    }

#pragma omp single nowait
    for (int src_row_1 =0; src_row_1 <extra2; src_row_1++) {
        for (int src_row_2 = src_row_1; src_row_2 < ny; src_row_2++) {
            float8_t cumsum0 = ZERO;
            for (int col = 0; col < nn; col++) {
                cumsum0 += (vd[nn * src_row_1 + col]) * (vd[nn * src_row_2 + col]);
            }
            result[src_row_2 + ny * src_row_1] = cumsum0[0] + cumsum0[1] + cumsum0[2] + cumsum0[3] +
                    cumsum0[4] + cumsum0[5] + cumsum0[6] + cumsum0[7];
        }
    }

#pragma omp for schedule(dynamic,1) nowait
    for (int src_row_1 = extra2; src_row_1 < ny; src_row_1 += 4) {
        for (int src_row_2 = src_row_1; src_row_2 < ny; src_row_2 += 4) {

			float8_t cumsum0 = ZERO;
            float8_t cumsum1 = ZERO;
            float8_t cumsum2 = ZERO;
            float8_t cumsum3 = ZERO;

            float8_t cumsum4 = ZERO;
            float8_t cumsum5 = ZERO;
            float8_t cumsum6 = ZERO;
            float8_t cumsum7 = ZERO;

            float8_t cumsum8 = ZERO;
            float8_t cumsum9 = ZERO;
            float8_t cumsum10 = ZERO;
            float8_t cumsum11 = ZERO;

            float8_t cumsum12 = ZERO;
            float8_t cumsum13 = ZERO;
            float8_t cumsum14 = ZERO;
            float8_t cumsum15 = ZERO;

            for (int col = 0; col < nn; col++) {

                cumsum0 += (vd[nn * src_row_1 + col]) * (vd[src_row_2 * nn + col]);
                cumsum1 += (vd[nn * src_row_1 + col]) * (vd[(src_row_2 + 1) * nn + col]);
                cumsum2 += (vd[nn * src_row_1 + col]) * (vd[(src_row_2 + 2) * nn + col]);
                cumsum3 += (vd[nn * src_row_1 + col]) * (vd[(src_row_2 + 3) * nn + col]);

                cumsum4 += (vd[(src_row_1 + 1) * nn + col]) * (vd[(src_row_2) * nn + col]);
                cumsum5 += (vd[(src_row_1 + 1) * nn + col]) * (vd[(src_row_2 + 1) * nn + col]);
                cumsum6 += (vd[(src_row_1 + 1) * nn + col]) * (vd[(src_row_2 + 2) * nn + col]);
                cumsum7 += (vd[(src_row_1 + 1) * nn + col]) * (vd[(src_row_2 + 3) * nn + col]);

                cumsum8 += (vd[(src_row_1 + 2) * nn + col]) * (vd[(src_row_2) * nn + col]);
                cumsum9 += (vd[(src_row_1 + 2) * nn + col]) * (vd[(src_row_2 + 1) * nn + col]);
                cumsum10 += (vd[(src_row_1 + 2) * nn + col]) * (vd[(src_row_2 + 2) * nn + col]);
                cumsum11 += (vd[(src_row_1 + 2) * nn + col]) * (vd[(src_row_2 + 3) * nn + col]);

                cumsum12 += (vd[(src_row_1 + 3) * nn + col]) * (vd[(src_row_2) * nn + col]);
                cumsum13 += (vd[(src_row_1 + 3) * nn + col]) * (vd[(src_row_2 + 1) * nn + col]);
                cumsum14 += (vd[(src_row_1 + 3) * nn + col]) * (vd[(src_row_2 + 2) * nn + col]);
                cumsum15 += (vd[(src_row_1 + 3) * nn + col]) * (vd[(src_row_2 + 3) * nn + col]);

            }
            result[src_row_2 + ny * src_row_1] =
                    cumsum0[0] + cumsum0[1] + cumsum0[2] + cumsum0[3] + cumsum0[4] + cumsum0[5] +
                    cumsum0[6] + cumsum0[7];
            result[src_row_2 + 1 + ny * (src_row_1)] =
                    cumsum1[0] + cumsum1[1] + cumsum1[2] + cumsum1[3] + cumsum1[4] + cumsum1[5] +
                    cumsum1[6] + cumsum1[7];
            result[src_row_2 + 2 + ny * (src_row_1)] =
                    cumsum2[0] + cumsum2[1] + cumsum2[2] + cumsum2[3] + cumsum2[4] + cumsum2[5] +
                    cumsum2[6] + cumsum2[7];
            result[src_row_2 + 3 + ny * (src_row_1)] =
                    cumsum3[0] + cumsum3[1] + cumsum3[2] + cumsum3[3] + cumsum3[4] + cumsum3[5] +
                    cumsum3[6] + cumsum3[7];

            result[src_row_2 + ny * (1 + src_row_1)] =
                    cumsum4[0] + cumsum4[1] + cumsum4[2] + cumsum4[3] + cumsum4[4] + cumsum4[5] +
                    cumsum4[6] + cumsum4[7];
            result[src_row_2 + 1 + ny * (1 + src_row_1)] =
                    cumsum5[0] + cumsum5[1] + cumsum5[2] + cumsum5[3] + cumsum5[4] + cumsum5[5] +
                    cumsum5[6] + cumsum5[7];
            result[src_row_2 + 2 + ny * (1 + src_row_1)] =
                    cumsum6[0] + cumsum6[1] + cumsum6[2] + cumsum6[3] + cumsum6[4] + cumsum6[5] +
                    cumsum6[6] + cumsum6[7];
            result[src_row_2 + 3 + ny * (1 + src_row_1)] =
                    cumsum7[0] + cumsum7[1] + cumsum7[2] + cumsum7[3] + cumsum7[4] + cumsum7[5] +
                    cumsum7[6] + cumsum7[7];

            result[src_row_2 + ny * (2 + src_row_1)] =
                    cumsum8[0] + cumsum8[1] + cumsum8[2] + cumsum8[3] + cumsum8[4] + cumsum8[5] +
                    cumsum8[6] + cumsum8[7];
            result[src_row_2 + 1 + ny * (2 + src_row_1)] =
                    cumsum9[0] + cumsum9[1] + cumsum9[2] + cumsum9[3] + cumsum9[4] + cumsum9[5] +
                    cumsum9[6] + cumsum9[7];
            result[src_row_2 + 2 + ny * (2 + src_row_1)] =
                    cumsum10[0] + cumsum10[1] + cumsum10[2] + cumsum10[3] + cumsum10[4] + cumsum10[5] +
                    cumsum10[6] + cumsum10[7];
            result[src_row_2 + 3 + ny * (2 + src_row_1)] =
                    cumsum11[0] + cumsum11[1] + cumsum11[2] + cumsum11[3] + cumsum11[4] + cumsum11[5] +
                    cumsum11[6] + cumsum11[7];
            result[src_row_2 + ny * (3 + src_row_1)] =
                    cumsum12[0] + cumsum12[1] + cumsum12[2] + cumsum12[3] + cumsum12[4] + cumsum12[5] +
                    cumsum12[6] + cumsum12[7];
            result[src_row_2 + 1 + ny * (3 + src_row_1)] =
                    cumsum13[0] + cumsum13[1] + cumsum13[2] + cumsum13[3] + cumsum13[4] + cumsum13[5] +
                    cumsum13[6] + cumsum13[7];
            result[src_row_2 + 2 + ny * (3 + src_row_1)] =
                    cumsum14[0] + cumsum14[1] + cumsum14[2] + cumsum14[3] + cumsum14[4] + cumsum14[5] +
                    cumsum14[6] + cumsum14[7];
            result[src_row_2 + 3 + ny * (3 + src_row_1)] =
                    cumsum15[0] + cumsum15[1] + cumsum15[2] + cumsum15[3] + cumsum15[4] + cumsum15[5] +
                    cumsum15[6] + cumsum15[7];

        }
    }

}//pr
    std::free(vd);
}

