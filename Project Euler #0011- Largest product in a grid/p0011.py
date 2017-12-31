#!/bin/python
import sys

grid = []
for grid_i in xrange(20):
    grid_temp = map(int,raw_input().strip().split(' '))
    grid.append(grid_temp)

data = grid
max = 0
for i in xrange(20):
	for j in xrange(20):
		if i<17:
			temp = data[i][j] * data[i+1][j] * data[i+2][j] + data[i+3][j]
			if max < temp:
				max = temp
				
		if j<17:
			temp = data[i][j] * data[i][j+1] * data[i][j+2] * data[i][j+3]
			if max < temp:
				max = temp
				
		if i<17 and j<17:
			temp = data[i][j] * data[i+1][j+1] * data[i+2][j+2] * data[i+3][j+3]
			if max < temp:
				max = temp
				
		if i<17 and j>2:
			temp = data[i][j] * data[i+1][j-1] * data[i+2][j-2] * data[i+3][j-3]
			if max < temp:
				max = temp
			
print(max)