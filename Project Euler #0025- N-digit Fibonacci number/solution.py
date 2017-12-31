MAX_DIGIT = 5000

data = {};
a, b = 0, 1
i = 0
while i >= 0:
	i += 1
	c = a + b
	a = b
	b = c
	
	if (len(str(a)) not in data):
		data[len(str(a))] = i
		
	if len(str(a)) == MAX_DIGIT:
		break

t = int(raw_input().strip())
for x in xrange(t):
	N = int(raw_input().strip())
	print data[N]