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
        BigInteger temp = BigInteger.ZERO;
            
        while(tCase-- > 0){
            temp = temp.add(new BigInteger(sc.next()));
        }
        String s = temp.toString();
        System.out.println(s.substring(0,10));

    }
}