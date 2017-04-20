import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        
        int max = n * (int)Math.pow(9, n);
        int sum = 0;
        for(int i=10; i<=max; i++){
            if(sumDigit(i, n) == i){
                sum += i;
            }
        }
        System.out.println(sum);
    }
    
    public static int sumDigit(int num, int pow){
        int sum = 0;
        int temp;
        
        while(num>0){
            temp = num%10;
            num /= 10;
            sum += (int) Math.pow(temp, pow);
        }
        
        return sum;
    }
}
