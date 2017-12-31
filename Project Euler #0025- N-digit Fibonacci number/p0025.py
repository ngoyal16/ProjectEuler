MAX_DIGIT = 1000
a, b = 0, 1
i = 0
while i >= 0:
	i += 1
	c = a + b
	a = b
	b = c
	if len(str(a)) == MAX_DIGIT:
		break
		
	
print i