# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def count_word(word): 
    return sum(ord(c) - 64 for c in word) 
    
name_string = raw_input().replace('"', '')
name_list = name_string.split(",")
name_list.sort()

res = 0
for i, val in enumerate(name_list):
	res += (i+1) * count_word(val)
	
print res
