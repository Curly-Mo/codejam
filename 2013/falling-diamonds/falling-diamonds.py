import fileinput
import sys
import math

def max(num):
	if num == 2:
		return num*2 + 1 + max(num-1)
	if num == 1:
		return 1
	return num*2 + 1 + max(num-2)

def triangleOfBase(num):
	if num < 1:
		return 0
	if num == 1:
		return 1
	return (num-1)*3 + triangleOfBase(num-3)

def numOperationsNeeded(armin, enemies):
	katamariSize = armin
	remaining = len(enemies) + 1
	operations = 0;
	for enemy in enemies:
		remaining -= 1
		if katamariSize > enemy:
			katamariSize += enemy
		else:
			ops = 0
			while katamariSize <= enemy:
				ops += 1
				if katamariSize - 1 > 0:
					katamariSize += katamariSize - 1
				else:
					break
			if ops >= remaining:
				operations += remaining
				return operations
			else:
				operations += ops
				if katamariSize > enemy:
					katamariSize += enemy


	return operations

infile=fileinput.input()
numCases=int(infile.readline())

for case in range(1,numCases+1):
	sys.stdout.write("Case #"+str(case)+": ")

	line = infile.readline().strip().split()

	numDiamonds=int(line[0])
	x=int(line[1])
	y=int(line[2])
	base=0
	max=0
	triangle=0
	probability = 0.0
	for num in range(0,numDiamonds+1):
		num = num*2-1
		triangle = triangleOfBase(num)
		if triangle == numDiamonds:
			base = num
			max = num
			triangle = triangleOfBase(base)
		if triangle > numDiamonds:
			max = num
			base = num-2
			triangle = triangleOfBase(base)
			break

	remaining = numDiamonds - triangle

	if x < base and y < base:
		probability = 1.0
	elif x > max or y > max:
		probability = 0.0
	else:
		probability = 100000.0

	print(probability)