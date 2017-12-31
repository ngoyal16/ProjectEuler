def factorial(num):
	if num <= 1:
		return 1
		
	else:
		return num*factorial(num-1)
		

t = int(raw_input().strip())
for a in xrange(t):
	N = int(raw_input().strip())
	print sum(int(c) for c in str(factorial(N)))
	