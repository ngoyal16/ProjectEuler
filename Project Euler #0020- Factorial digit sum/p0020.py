def factorial(num):
	if num == 1:
		return 1
		
	else:
		return num*factorial(num-1)
		
N = 100
print sum(int(c) for c in str(factorial(N)))