import math

def isPrime(n):
	if n == 2:
		return True
		
	if n % 2 == 0 or n <= 1:
		return False
		
	sqr = int(math.sqrt(n)) + 1
	for divisor in range(3, sqr, 2):
		if n % divisor == 0:
			return False
			
	return True	

num = 2
currentPrime = 1
while currentPrime < 10001:
	num += 1
	if isPrime(num):
		currentPrime += 1
	
print num