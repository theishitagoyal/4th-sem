#include <stdio.h>
#include <string.h>
#define MAX 256

void shiftTable(char pattern[], int table[]){
    int m = strlen(pattern);
    for (int i = 0; i<MAX; i++){
        table[i]=m;
    }
    for (int i = 0; i<m-1; i++){
        table[(unsigned char)pattern[i]] = m-i-1;
    }
}
void horspool(char text[], char pattern[], int table[]){
    int n = strlen(text);
    int m = strlen(pattern);
    int i = m-1;
    int found = 0;
    while (i<n){
        int k = 0;
        while (k<n && pattern[m-1-k]==text[i-k]){
            k++;
        }
        if (k==m) {
            printf("Pattern found at %d position\n", i-m+2);
            found = 1;
            i++;
        }
        else {
            i+=table[(unsigned char)text[i]];
        }
    }
    if (found==0){
        printf("Pattern not found\n");
    }
}
void main(){
    char text[MAX], pattern[MAX];
    int table[MAX];
    printf("Enter source string: ");
    scanf("%s", text);
    printf("Enter pattern string: ");
    scanf("%s", pattern);
    shiftTable(pattern, table);
    horspool(text, pattern, table);
}
