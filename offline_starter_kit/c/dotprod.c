#include <stdio.h>
#include <stdlib.h>
#include <time.h>

double dot(const double* a, const double* b, int n){
    double s = 0.0;
    for(int i=0;i<n;i++) s += a[i]*b[i];
    return s;
}

int main(){
    int n = 1000000;
    double *a = malloc(sizeof(double)*n);
    double *b = malloc(sizeof(double)*n);
    for(int i=0;i<n;i++){ a[i] = i%13; b[i] = (i%17)*0.5; }
    clock_t t0 = clock();
    double s = dot(a,b,n);
    clock_t t1 = clock();
    printf("dot=%.2f time=%.3fs\n", s, (double)(t1-t0)/CLOCKS_PER_SEC);
    free(a); free(b);
    return 0;
}
