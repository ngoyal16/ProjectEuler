#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int caseT, N, i, min=1;
    scanf("%d",&caseT);
    while(caseT--){
        scanf("%d",&N);
        min=N;
        for(i=1; i<=N; i++){
            if(min%i == 0) continue;
            int temp=i;
            for(int j=2; j<temp; j++){
                if(temp%j == 0){
                    temp /= j;
                    j--;
                }
            }
           min *= temp;
        }
        printf("%d\n",min);
    }
    return 0;
}
