import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        
        Scanner sc = new Scanner(System.in);
        int t =1;
        try{
            t = sc.nextInt();
                
        }catch (InputMismatchException e) {
        }
        
        BigInteger n = new BigInteger("0");
        BigInteger temp = new BigInteger("0");
        for(int i=0; i<t; i++){
           try{
               n = sc.nextBigInteger();
               n = n.subtract(BigInteger.valueOf(1));
             }catch (InputMismatchException e) {
           }
            
            temp = sum_multiples(BigInteger.valueOf(3), n);
            temp = temp.add(sum_multiples(BigInteger.valueOf(5), n));
            temp = temp.subtract(sum_multiples(BigInteger.valueOf(15), n));
            
            System.out.println(temp);
        }
    }
    
    public static BigInteger sum_multiples(BigInteger x, BigInteger number){
		BigInteger sum = number.divide(x);
        BigInteger t = sum.add(BigInteger.valueOf(1));
        
        sum =  x.multiply(sum.multiply(t));
        sum =  sum.divide(BigInteger.valueOf(2));
        
        return sum;
	}
}