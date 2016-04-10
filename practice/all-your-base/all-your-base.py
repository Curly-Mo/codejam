import fileinput
import sys
import math

def toMinValue(word,base):
	symbols = "1023456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	value = ""
	count=0
	usedChars = {}
	for char in word:
		if char in usedChars:
			value += usedChars[char]
		else:
			value += symbols[count]
			usedChars[char] = symbols[count]
			count += 1
	return value

def numUniqueChars(s):
	count=0
	chars=[]
	for c in s:
		if c not in chars:
			count+=1
			chars.append(c)
	return count

infile=fileinput.input()
numCases=int(infile.readline())

board = [[0 for x in range(4)] for x in range(4)] 
for case in range(1,numCases+1):
	sys.stdout.write("Case #"+str(case)+": ")

	line = infile.readline().strip()

	base = numUniqueChars(line)
	if base < 2:
		base = 2

	value = toMinValue(line,base)

	#print(value)
	print(str(int(value, base)))

