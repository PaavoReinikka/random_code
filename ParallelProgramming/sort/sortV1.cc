#include "so.h"
#include <algorithm>
#include <omp.h>
#include <iostream>


inline void swap(data_t *a, int low, int high) {
    data_t temp=a[low];
    a[low]=a[high];
    a[high]=temp;
}

inline void insertionsort(data_t * a, const int lo, const int hi)
{
    for(int i = lo; i < hi; ++i) {
        for(int j = i; j > lo; --j) {
            if(a[j] < a[j-1]) swap(a, j-1, j);
            else break;
        }
    }
}

int pOtwo(int n)
{
    return (n & (~(n - 1)));
}

int highestPowerof2(int n)
{
    int res = 0;
    for (int i=n; i>=1; i--)
    {
        // If i is a power of 2
        if ((i & (i-1)) == 0)
        {
            res = i;
            break;
        }
    }
    return res;
}

void quickishsort(data_t * X, int n, int depth, int critical)
{
    if (depth<critical) {
		depth++;
		std::nth_element(X, X+n/2, X+n);
#pragma omp parallel sections
{
#pragma omp section
        quickishsort(X, n / 2, depth, critical);
#pragma omp section
        quickishsort(X + (n / 2), n - (n / 2), depth, critical);
}
    } else {
		std::sort(X,X+n);
    }

}

void psort(int n, data_t* data) {

//If small list -> use seq. sorting
    if (n < 100) {
        std::sort(data, data + n);
        return;
    }

    int t = omp_get_max_threads();
    int tt = highestPowerof2(t);

    int critical = 0;
    int leaves = 1;
    int branches = 2;
    while(tt > leaves)
    {
        critical++;
        leaves *= branches;
    }

	t=2*t;
	int block=n/t;

//Quicksort benefits from partially ordered lists
#pragma omp parallel for schedule(dynamic)
	for (int i=0;i<t;i++) {
		std::nth_element(data+i*block, data+i*block+block/2, data+(i+1)*block);

	}

	omp_set_nested(1);
    quickishsort(data, n, 0,critical);

}

