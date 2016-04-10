import fileinput
import sys
import math

def isSolvable(armin, enemies):
	katamariSize=armin
	for enemy in enemies:
		if katamariSize > enemy:
			katamariSize += enemy
		else:
			return False
	return True

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



	print(numOperationsNeeded(armin, enemies))

