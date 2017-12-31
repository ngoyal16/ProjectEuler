# Enter your code here. Read input from STDIN. Print output to STDOUT
data = {}

def countFactor(n):
    return set(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

t = 1
traingle = 1
n = 1

def calculateTriangle(num):
	global t
	global traingle
	global n
	
	#print('hello')
	
	while 1:
		res = len(countFactor(traingle))
		if res not in data:
			for x in range(t, res):
				data[x] = traingle
				t += 1
			
		if res > num:
			#return traingle
			return
		
        #print(i, traingle)
		n += 1
		traingle += n
		#print(i, traingle)
		
	
min_point = 526

if min_point not in data:
	calculateTriangle(min_point)
	
#print(data)
print data[min_point]
