#include <stdio.h>
#include <stdlib.h>
#define MAX 20
#define INF 10000
int dist[MAX][MAX];
int v;

void fw(){
    for (int k=0; k<v; k++){
        for (int i=0; i<v; i++){
            for (int j=0; j<v; j++){
                if (dist[i][k]+dist[k][j]<dist[i][j]){
                    dist[i][j]=dist[i][k]+dist[k][j];
                }
            }
        }
    }
}

void main(){
    int E;
    int i, j;
    printf("Enter no. of edges and vertices: ");
    scanf("%d %d", &E, &v);
    for (i=0; i<v; i++){
        for (j=0; j<v; j++){
            if (i==j){
                dist[i][j]=0;
            }
            else {
                dist[i][j] = INF;
            }
        }
    }
    printf("Enter the source, destination, weight of edges: \n");
    for (i=0; i<E; i++){
        int s, d, w;
        scanf("%d %d %d", &s, &d, &w);
        dist[s][d]=w;
    }
    fw();
    for (i=0; i<v; i++){
        for (j=0; j<v; j++){
            if (dist[i][j]==INF){
                printf("\tINF");
            }
            else {
                printf("\t%d", dist[i][j]);
            }
        }
        printf("\n");
    }
}
