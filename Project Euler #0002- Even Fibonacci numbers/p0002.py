limit = 4000000
sum = 0
a = 1
b = 1
c = a + b
while c < limit:
	sum += c
	a = b + c
	b = c + a
	c = a + b
	
print sum