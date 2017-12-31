def palindrome(num):
    return str(num) == str(num)[::-1]
	
max_palindrom = 0;
for i in range(100, 1000):
	for j in range(100, 1000):
		n = i*j
		if palindrome(n) and max_palindrom < n:
			max_palindrom = n
			
print max_palindrom