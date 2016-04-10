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

	line1 = infile.readline().strip().split()

	energy=int(line1[0])
	regain=int(line1[1])
	numActivities=int(line1[2])
	activities=infile.readline().stri().split()
	activities=[int(x) for x in activities]
	sortedActivities=sorted(activities)

	totalEnergy=energy+regain*len(activities)
	gain=0

	for activity in activities:
		gain += activity*regain

	average = sum(activities)/len(activities)

	print(totalEnergy*average)

