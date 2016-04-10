import fileinput
import sys


infile=fileinput.input()
numCases=int(infile.readline())

for case in range(1,numCases+1):
	sys.stdout.write("Case #"+str(case)+": ")

	line = infile.readline().strip().split()
	numKeys = int(line[0])
	numChests = int(line[1])
	keys = infile.readline().strip().split()
	

	for n in range(0,numChests):
		chest = infile.readline().strip().split()
		chestKeyType = chest.pop()
		chestNumKeys = chest.pop()
		chestKeys = chest
		print(chest)