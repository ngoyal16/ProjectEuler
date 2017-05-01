max_limit = 28124
data = [1] * max_limit
data[0] = 0
abundantNum = []
for i in range(2, max_limit):
	for j in range(i*2, max_limit, i):
		data[j] += i
		
	if data[i] > i:
		abundantNum.append(i)

for i in abundantNum:
	for j in abundantNum:
		if i+j >= max_limit :
			break
			
		data[i+j] = 0

print sum(i for (i, x) in enumerate(data) if x)