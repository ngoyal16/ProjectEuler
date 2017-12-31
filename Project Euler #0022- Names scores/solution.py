# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def count_word(word): 
    return sum(ord(c) - 64 for c in word) 
    
name_list = []
count_name = int(raw_input())

for x in range(0, count_name):
    name_list.extend([raw_input()])

name_list.sort()

count_check = int(raw_input())
for x in range(0, count_check):
    check_name = raw_input()
    print((name_list.index(check_name) + 1) * count_word(check_name))