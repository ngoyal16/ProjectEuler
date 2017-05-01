data = {1:1}

def calculateCollatz(num):
	if num not in data:
		if(num%2 == 0):
			temp = num/2
			
		else :
			temp  = num*3 + 1
			
		data[num] = calculateCollatz(temp) + 1
		
	return data[num]
	
print max(range(1, 1000000), key=calculateCollatz)
	