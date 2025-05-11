#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 100

int adj[MAX][MAX], indegree[MAX], topOrder[MAX];

void createAdj(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i < j) {
                adj[i][j] = rand() % 2;
            } else {
                adj[i][j] = 0;
            }
        }
    }
}

void calcIndegree(int n) {
    for (int i = 0; i < n; i++) {
        indegree[i] = 0;
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (adj[j][i] == 1) {
                indegree[i]++;
            }
        }
    }
    printf("Initial indegrees - \n");
    for (int i = 0; i<n; i++){
        printf("%c : %d\n", i+'A', indegree[i]);
    }
}

void toposort(int n) {
    int count = 0;
    int index = 0;
    printf("Topological sorting:\n");
    while (count < n) {
        int found = 0;
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                printf("Selected Node: %c\n", i + 'A');
                topOrder[index++] = i;
                indegree[i] = -1;
                for (int j = 0; j < n; j++) {
                    if (adj[i][j] == 1) {
                        indegree[j]--;
                        printf("Indegree of %c reduced to %d\n", j + 'A', indegree[j]);
                    }
                }
                count++;
                found = 1;
                break;
            }
        }
        if (!found) {
            printf("Cyclic graph detected\n");
            return;
        }
    }
    printf("Topological Order:\n");
    for (int i = 0; i < n; i++) {
        printf("%c\t", 'A' + topOrder[i]);
    }
    printf("\n");
}

int main() {
    int n;
    printf("Enter no. of nodes: ");
    scanf("%d", &n);
    srand(time(NULL));
    createAdj(n);
    
    printf("Adjacency matrix:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d\t", adj[i][j]);
        }
        printf("\n");
    }

    calcIndegree(n);
    toposort(n);
    return 0;
}
