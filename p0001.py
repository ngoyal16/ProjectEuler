target = 999

def sumDivisibleBy(n):
	p = target / n;
	return n*(p*(p+1)/2)
	
print sumDivisibleBy(3) + sumDivisibleBy(5) - sumDivisibleBy(15)