ONES = [" Zero", " One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine", " Ten", " Eleven", " Twelve", " Thirteen", " Fourteen", " Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen"]
TENS = ["", "", " Twenty", " Thirty", " Forty", " Fifty", " Sixty", " Seventy", " Eighty", " Ninety"]

def to_english(n):
	if 0 <= n < 20:
		return ONES[n]
		
	elif 20 <= n < 100:
		return TENS[n/10] + (ONES[n%10] if (n%10 != 0) else "")
	
	elif 100 <= n < 1000:
		return to_english(n // 100) + " Hundred" + (to_english(n%100) if (n%100 != 0) else "")
		
	elif 1000 <= n < 1000000:
		return to_english(n // 1000) + " Thousand" + (to_english(n%1000) if (n%1000 != 0) else "")
		
	elif 1000000 <= n < 1000000000:
		return to_english(n // 1000000) + " Million" + (to_english(n%1000000) if (n%1000000 != 0) else "")
		
	elif 1000000000 <= n < 1000000000000:
		return to_english(n // 1000000000) + " Billion" + (to_english(n%1000000000) if (n%1000000000 != 0) else "")

t = int(raw_input().strip())
for a in xrange(t):
	num = int(raw_input().strip())
	print to_english(num).strip()