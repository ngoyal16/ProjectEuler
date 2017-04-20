import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Solution sol = new Solution();
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        while(T-- > 0){
            int n = in.nextInt();
            sol.calcPrime(n);
            System.out.println(sol.getSum(n));
        }
    }
    
    ArrayList<Long> arr = new ArrayList<Long>();
    long counter = 4;
    public void calcPrime(int inp) {
        if(arr.size() == 0){
            long val = 2;
            arr.add(val);
        }
        if(arr.size() == 1){
            long val = 3;
            arr.add(val);
        }
       
        if(counter > inp){
            return;
        }

        while(counter <= inp) {
            if(counter % 2 != 0 && counter%3 != 0) {
                int temp = 4;
                while(temp*temp <= counter) {
                    if(counter % temp == 0)
                        break;
                    temp ++;
                }
                if(temp*temp > counter) {
                    arr.add(counter);
                }
            }
            counter++;
        }
        
        return;
    }
    
    public long getSum(long n){
        if(arr==null || arr.size()<1)
            return 0;

        long sum = 0;
        for(Long i: arr){
            if(i > n){
                return sum;
            }
            sum = sum+i;
        }
            
        return sum;
    }
}