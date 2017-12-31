# Enter your code here. Read input from STDIN. Print output to STDOUT
L = input()    
d = 10   # last d digits of series
s = sum(pow(n, n, 10**d) for n in range(1, L+1))
 
print (s%10**d)