def calCulateGridMax(triangle):
	for i in reversed(range(len(triangle) - 1)):
		for j in range(len(triangle[i])):
			triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
			
	return triangle[0][0]



t = int(raw_input().strip())
for a in xrange(t):
	N = int(raw_input().strip())
	triangle = []
	for triangle_i in xrange(N):
		triangle_temp = map(int,raw_input().strip().split(' '))
		triangle.append(triangle_temp)

	print calCulateGridMax(triangle)