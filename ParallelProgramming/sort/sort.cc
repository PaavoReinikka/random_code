#include "so.h"
#include <algorithm>
#include <omp.h>
#include <iostream>



int pOtwo(int n) 
{ 
    return (n & (~(n - 1))); 
} 


// "manual" mergesort: first partitions are sorted in for loop
// ,then merged in another for loop
void psort(int n, data_t* data) {

//If small list -> use seq. sorting
   if (n<100) {
	std::sort(data, data + n);
	return;
   }

   bool flag=false;
//If n is odd, subtracts one and flags it
   if (n%2==1) {
	--n;
	flag=true;
   }

   int po2=pOtwo(n);
   int t = omp_get_max_threads();

//gives max threads in an ideal case.
   if (t == pOtwo(t) && n%t==0) po2=t;

   int rem=n%po2;
   int block=n/po2;

//number of loops is a power of 2 -> threadcount
   #pragma omp parallel for schedule(static,1)
   for (int i=0;i<po2;i++) {
	std::sort(data+i*block,data+(i+1)*block);
   }
//outer loop is merging iteratively.
   for (int j=block; j<n ; j*=2) {
   #pragma omp parallel for schedule(static,1)
	for (int k=0;k<po2;k+=2) {
	    std::inplace_merge(data+k*j,data+(k+1)*j,data+(k+2)*j);
	}
	po2/=2;
   }

//takes care of the remainder and the n-1
   if (rem || flag) {
	if (flag) {
		rem++;n++;
        }
	std::sort(data + n - rem, data + n);
	std::inplace_merge(data,data+n-rem,data+n);
   }

}


