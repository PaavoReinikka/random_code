#include "cp.h"
#include <math.h>
#include <cstdlib>
#include <iostream>
#include <cuda_runtime.h>
#include <stdlib.h>


#define TILE_WIDTH 16

inline void check(cudaError_t err, const char* context) {
    if (err != cudaSuccess) {
        std::cerr << "CUDA error: " << context << ": "
            << cudaGetErrorString(err) << std::endl;
        std::exit(EXIT_FAILURE);
    }
}
#define CHECK(x) check(x, #x)

inline int static divup(int a, int b) {
    return (a + b - 1)/b;
}

inline int static roundup(int a, int b) {
    return divup(a, b) * b;
}

/*

__global__ void mykernel(float *res, float *data, int ny, int nx) {

	int row1=(blockIdx.y*blockDim.y+threadIdx.y);
	int row2=(blockIdx.x*blockDim.x+threadIdx.x);
	if (row1>row2 || row2 >=ny) {return;}
	
	float cumsum = 0.0;
	for (int col=0;col<nx;++col) {
		cumsum+=data[row1*nx+col]*data[row2*nx+col];
	}
	res[row1*ny+row2]=cumsum;
}
*/

__global__ void mykernel(float* res, float *data, int nx)
{
	//everything is preprocessed to fit nicely into square blocks
	__shared__ float shared_1[TILE_WIDTH*TILE_WIDTH];
	__shared__ float shared_2[TILE_WIDTH*TILE_WIDTH];

	int tx = threadIdx.x;
	int ty = threadIdx.y;
	
	int row1 = blockIdx.y * TILE_WIDTH + ty;//threadIdx.y;
	int row2 = blockIdx.x * TILE_WIDTH + tx;//threadIdx.x;
	
	//preprocessing quarantees otherwise we stay within bounds
	// and this takes the upper diagonal
	if(row1>row2+TILE_WIDTH) return;
	float cumsum = 0;

	for (int i = 0; i < nx/TILE_WIDTH; ++i) {
		shared_1[ty*TILE_WIDTH+tx] = data[row1*nx + i*TILE_WIDTH + tx];
		shared_2[ty*TILE_WIDTH+tx] = data[i*TILE_WIDTH + ty+row2*nx];
		__syncthreads();
		
		for (int j = 0; j < TILE_WIDTH; ++j)
			cumsum += shared_1[ty*TILE_WIDTH+j] * shared_2[j*TILE_WIDTH+tx];
			__syncthreads();
		}
		res[row1*nx+row2] = cumsum;
}
void correlate(int ny, int nx, const float* data, float* result) {

    int threadsY=TILE_WIDTH;
    int threadsX=TILE_WIDTH;
    float s,ss;
	int NX=roundup(nx,TILE_WIDTH);
	int NY=roundup(ny,TILE_WIDTH);
	
	if(NX>NY) NY=NX; else NX=NY;

	float *temp = new float[NX*NY];
	float *temp2 = new float[NY*NY];

    for (int row=0;row<ny;row++) {
		s=0.0;
		for (int col=0;col<nx;col++) {
			s=s+data[nx*row+col];
		}
		ss=0.0;
		s/=nx;
		for (int col=0;col<nx;col++) {
			double elem = data[nx*row+col]-s;
			ss=ss+pow(elem,2);
			temp[NX*row+col]=elem;
		}
		ss=1.0/sqrt(ss);
		for (int col=0;col<nx;col++) {
			temp[NX*row+col]=ss*temp[NX*row+col];
		}
		for (int col=nx;col<NX;col++) temp[NX*row+col]=0.0f;
    }

    for(int row=ny;row<NY;row++)
	for(int col=0;col<NX;col++) temp[NX*row+col]=0.0f;

    float *dGPU = NULL;
    CHECK(cudaMalloc((void**)&dGPU, NY * NX * sizeof(float)));

    float *rGPU = NULL;
    CHECK(cudaMalloc((void**)&rGPU, NY * NY * sizeof(float)));
    CHECK(cudaMemcpy(dGPU, temp, NY * NX * sizeof(float), cudaMemcpyHostToDevice));

    dim3 dimBlock(threadsX, threadsY);
    dim3 dimGrid(divup(NY,threadsX), divup(NY, threadsY));

    mykernel<<<dimGrid, dimBlock>>>(rGPU, dGPU, NX);
    CHECK(cudaGetLastError());

	//IF HAPPENED TO BE SQUARE MATRIX, AND DIVISIBLE BY TILE_WIDTH
	// DON'T BOTHER USING temp2 BUT COPY DIRECTLY TO result	
    if(nx==NY) {
	CHECK(cudaMemcpy(result, rGPU, NY * NY * sizeof(float), cudaMemcpyDeviceToHost));
	CHECK(cudaFree(dGPU));
	CHECK(cudaFree(rGPU));
    } else {
	CHECK(cudaMemcpy(temp2, rGPU, NY * NY * sizeof(float), cudaMemcpyDeviceToHost));
	CHECK(cudaFree(dGPU));
	CHECK(cudaFree(rGPU));
	for(int row=0;row<ny;row++) {
	    for(int col=row;col<ny;col++) {
		result[row*ny+col]=temp2[row*NY+col];
	    }
	}
    }

    delete [] temp;delete [] temp2;
}


