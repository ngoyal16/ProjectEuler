listN = range(999, 99, -1)
def isPalindrome(num):
    return str(num) == str(num)[::-1]
	
def getDivisor(num):
	global listN
	for i in listN:
		for j in listN:
			if i*j == num:
				return 1
	return 0

t = int(raw_input().strip())
for a in xrange(t):
	max = int(raw_input().strip())-1
	while(max > 101101):
		if isPalindrome(max) and getDivisor(max):
			break
		max -= 1
		
	print max