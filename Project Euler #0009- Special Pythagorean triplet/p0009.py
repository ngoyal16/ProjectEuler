n = 100
res = -1
if n > 5 and n%2 == 0:
	temp = n/3
	
	for i in range(1, temp):
		j = (n*(n-2*i))/(2*(n-i))
		k = n - j - i
		if j >= k:
			continue

		if((i*i + j*j) == (k*k)):
			temp = i*j*k
			if temp > res:
				res = temp
print(res)