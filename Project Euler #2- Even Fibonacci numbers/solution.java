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
        for(int i=0; i<t; i++){
           try{
               n = sc.nextBigInteger();
               
             }catch (InputMismatchException e) {
           }
            System.out.println(fabonic(n));
        }
    }
    
    public static BigInteger fabonic(BigInteger Number){
        BigInteger fib1 = new BigInteger("0");
        BigInteger fib2 = new BigInteger("1");
        BigInteger sum = new BigInteger("0");
        BigInteger bigTwo = new BigInteger("2");
        
        BigInteger fib = new BigInteger("0");
		while(Number.compareTo(fib) > 0)
		{
            if (fib.remainder(bigTwo).equals(BigInteger.ZERO))
                   sum = sum.add(fib);
            fib = fib1.add(fib);
            fib1 = fib2;
            fib2 = fib;
		}
        return sum;
	}
}