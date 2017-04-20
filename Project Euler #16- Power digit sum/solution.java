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
        BigInteger temp = new BigInteger("2");
        BigInteger t1;
        while(tCase-- > 0){
            t1 = temp.pow(sc.nextInt());
            String data = t1.toString();
            
            int sum = 0;
            for(int i = 0; i < data.length(); i++) {
                if(Character.isDigit(data.charAt(i))) {
                    sum += Integer.parseInt(""+data.charAt(i));
                }
            }
            System.out.println(sum);
        }
    }
}