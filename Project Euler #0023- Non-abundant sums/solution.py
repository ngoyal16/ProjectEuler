max_limit = 28124
data = [1] * max_limit
data[0] = 0
abundantNum = []
for i in range(2, max_limit):
	for j in range(i*2, max_limit, i):
		data[j] += i
		
	if data[i] > i:
		abundantNum.append(i)

res = [False] * max_limit
for i in abundantNum:
	for j in abundantNum:
		if i+j >= max_limit :
			break
			
		res[i+j] = True

t = int(raw_input().strip())
for a in xrange(t):
	num = int(raw_input().strip())
	if num >= max_limit or res[num]:
		print 'YES'
	else:
		print 'NO'