#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int caseT;
    unsigned long long N, i, maxDiv;
    scanf("%d",&caseT);
    while(caseT--){
        scanf("%llu",&N);
        while(N%2==0 && N!=1 ){
            N/=2;
        }
        if (N==1){
             N=2;
        }else{
            while(N%3==0 && N!=1 ){
                N/=3;
            }
            if (N==1){
                N = 3;
            }else{
                maxDiv = sqrt(N)+1;
                for(i = 6; (i-1)<=maxDiv; i+=6){
                    while(N%(i-1)==0 && N!=1){
                        N /= (i-1);
                    }
                    if(N == 1){
                        N = (i-1);
                    }
                    
                    while(N%(i+1)==0 && N!=1){
                        N /= (i+1);
                    }
                    if(N == 1){
                        N = (i+1);
                    }
                    maxDiv = sqrt(N)+1;
                }
            }
        }
        printf("%llu\n",N);
    }
    return 0;
}
