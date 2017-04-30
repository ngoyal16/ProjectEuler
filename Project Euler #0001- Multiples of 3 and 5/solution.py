target = 1

def sumDivisibleBy(n):
	global target
	p = (target-1) / n;
	return n*(p*(p+1)/2)

	
t = int(raw_input().strip())
for i in xrange(t):
	target = int(raw_input().strip())
	print sumDivisibleBy(3) + sumDivisibleBy(5) - sumDivisibleBy(15)