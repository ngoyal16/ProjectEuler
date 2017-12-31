num = 600851475143
if num%2 == 0:
	factor = 2
	num /= 2
	while num%2==0:
		num /= 2
else:
	factor = 1
	
n = 3
max = num**0.5
while num>1 and n<=max:
	if num%n == 0:
		num /= n
		factor = n
		while num%n == 0:
			num /= n
			
		max = num**0.5
		
	n += 2
	
if num==1:
	print factor
else:
	print num