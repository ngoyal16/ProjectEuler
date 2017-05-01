min = 20
for i in range(1, min+1):
	if(min%i == 0):
		continue
	
	temp = i
	j = 2
	while j<temp:
		if(temp%j == 0):
			temp /= j
			j -= 1
		j += 1
		
	min *= temp;


print min