import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        
        int tCase = sc.nextInt();
        
        while(tCase-- > 0){
            BigInteger temp, t1, t2, t3;
            int n = sc.nextInt(); 
            temp = new BigInteger(String.valueOf(n));
            //n(n+1)/2
            t1 = (temp.multiply(temp.add(BigInteger.ONE))).divide(new BigInteger("2"));
            
            //n(n+1)(2n+1)/6
            t2 = (((temp.multiply(new BigInteger("2"))).add(BigInteger.ONE)).multiply(t1)).divide(new BigInteger("3"));
            
            t3 = (t1.pow(2)).subtract(t2);
            System.out.println(t3.abs());
        }
    }
}