import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        while(T-- > 0){
            int n = in.nextInt();
            int k = in.nextInt();
            String str = in.next();
            char arr[] = str.toCharArray();
            long maxMultiply = 0;
            
            for(int i=0; i<(arr.length-(k-1)); i++){
                long currentMultiply = 1;
                for(int j=0; j<k; j++){
                    currentMultiply *= (arr[i+j] - 48);
                }
                
                if(currentMultiply > maxMultiply){
                    maxMultiply = currentMultiply;
                }
            }
            
            System.out.println(maxMultiply);
        }
    }
}