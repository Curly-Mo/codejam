import fileinput
import sys
import math

def rotate(word):
    return  word[-1:] + word[:-1] 

def getWinner(board,dimension,numToWin):
	return "Neither"

infile=fileinput.input()
numCases=int(infile.readline())

for case in range(1,numCases+1):
	sys.stdout.write("Case #"+str(case)+": ")

	line = infile.readline().strip().split()

	radius=int(line[0])
	paint=int(line[1])
	minimum= math.floor(math.sqrt(paint-radius))
	r = radius+(math.floor(minimum/2))*2
	print(r)
	remainingPaint = paint - (r*r/2 - radius*radius)
	print(remainingPaint)
	r+=2
	count = 1
	#print(remainingPaint)
	while remainingPaint >= r*r - (r-1)*(r-1):
		count+=1
		remainingPaint -= r*r - (r-1)*(r-1)
		r += 2


	print(count)

