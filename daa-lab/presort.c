#include <stdio.h>
#include <sys/time.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#define MAX 1000

int partition(int A[MAX], int l, int r){
    int pivot = A[l];
    int i = l+1;
    int j = r;
    while (1){
        while (pivot<A[i] && i<=j){
            i++;
        }
        while (pivot>A[j]){
            j--;
        }
        if (i<j){
            int temp = A[i];
            A[i] = A[j];
            A[j] = temp;
        }
        else {
            A[l] = A[j];
            A[j] = pivot;
            return j;
        }
    }
}

void quicksort(int A[MAX], int l, int r){
    if (l<r){
        int s = partition(A, l, r);
        quicksort(A, l, s-1);
        quicksort(A, s+1, r);
    }
}

bool presortelementunique(int A[MAX], int n){
    quicksort(A, 0, n-1);
    for (int i = 0; i<n-1; i++){
        if (A[i]==A[i+1]){
            return false;
        }
    }
    return true;
}

void main(){
    int arr[MAX], n;
    printf("size of array: ");
    scanf("%d", &n);
    struct timeval start, end;
    srand(time(NULL));
    for (int i = 0; i<n; i++){
        arr[i] = rand()%201;
        printf("%d\t", arr[i]);
    }
    gettimeofday(&start, NULL);
    bool ans = presortelementunique(arr, n);
    gettimeofday(&end, NULL);
    long sec = end.tv_sec - start.tv_sec;
    long usec = end.tv_usec - start.tv_usec;
    double time = sec + usec*1e-6;
    printf("time taken = %.6f\n", time);
    if (ans == true){
        printf("All elements unique");
    }
    else {
        printf("not unique");
    }
}
