n = 100

# n(n+1)/2 = 1 + 2 + 3 + ... + n
sumOfNumber = n*(n+1)/2

# n(n+1)(2n+1)/6 = 1^2 + 2^2 + 3^3 + .... + n^2
sumOfSqure = sumOfNumber*(2*n+1)/3

print sumOfNumber**2 -sumOfSqure