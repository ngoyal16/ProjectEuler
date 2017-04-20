#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int reverse(int value) {
    int result = 0;
    while (value != 0) {
        result *= 10;
        result += value % 10;
        value /= 10;
    }
    return result;
}

int getDivisor(int temp){
    int i, j;
    for(i=999; i>=100; i--){
        for(j=999; j>=100; j--){
            if(i*j == temp){
                return 1;
            }
        }
    }
    return 0;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int caseT, N, i;
    
    scanf("%d",&caseT);
    while(caseT--){
        scanf("%d",&N);
        
        for(i=N-1; i>101101; i--){
            if((i == reverse(i)) && getDivisor(i)){
                break;
                
            }
        }
        printf("%d\n",i);
    }
    return 0;
}
