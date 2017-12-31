def calEvenFabonacciSum(limit):
	sum = 0
	a = 1
	b = 1
	c = a + b
	while c < limit:
		sum += c
		a = b + c
		b = c + a
		c = a + b
		
	return sum
	

t = int(raw_input().strip())
for i in xrange(t):
	print calEvenFabonacciSum(long(raw_input().strip()))
