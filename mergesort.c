#include <stdio.h>
#include <sys/time.h>
#include <stdlib.h>
/*void display(int arr[], int n){
    for (int i = 0; i<n; i++){
        printf("%d\t", arr[i]);
    }
    printf("\n");
}*/
void merge(int arr[], int p, int q, int r){
    int n1 = q-p+1;
    int n2 = r-q;
    int L[52], R[52];
    for (int i = 0; i<n1; i++){
        L[i] = arr[p+i];
    }
    for (int i = 0; i<n2; i++){
        R[i] = arr[q+i+1];
    }
    int i = 0, j = 0, k = p;
    while (i<n1 && j<n2){
        if (L[i]<R[j]){
            arr[k++] = L[i++];
        }
        else if (L[i]>R[j]){
            arr[k++] = R[j++];
        }
        else {
            arr[k++] = L[i++];
            arr[k++] = R[j++];
        }
        if (i==n1 && j<n2){
            while (j!=n2){
                arr[k++] = R[j++];
            }
        }
        else if (j==n2 && i<n1){
            while (i!=n1){
                arr[k++] = L[i++];
            }
        }
    }
}
void mergesort(int arr[10], int p, int r){
    if (p<r){
        int q = (p+r)/2;
        mergesort(arr, p, q);
        mergesort(arr, q+1, r);
        merge(arr, p, q, r);
    }
}
void main(){
    int arr[10000], n = 100;
    struct timeval start, end;
    //srand(time(NULL));
    //printf("Enter array size: ");
    //scanf("%d", &n);
    for (int i = 1;i<11; i++){
        for (int j = 0; j<n*i; j++){
            arr[i] = rand()%201;
        }
        gettimeofday(&start, NULL);
        mergesort(arr, 0, n*i);
        gettimeofday(&end, NULL);
        long sec = end.tv_sec - start.tv_sec;
        long usec = end.tv_usec - start.tv_usec;
        double time = sec + usec*1e-6;
        printf("for array of size %d time taken = %.6f\n", n*i, time);
    }
}
