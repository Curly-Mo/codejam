import fileinput
import sys
import math

def isPalindrome(num):
	word = str(num)
	#print(word)
	if word == word[::-1]:
		return True
	else:
		return False

#def generatePalindromes(min, max):
#	palindromes=[]
#	s=str(min)
#	if len(s) % 2 == 0:
#		half=s[:len(s)/2]
#		attempt=""
#		while()

infile=fileinput.input()
numCases=int(infile.readline())

board = [[0 for x in range(4)] for x in range(4)] 
for case in range(1,numCases+1):
	sys.stdout.write("Case #"+str(case)+": ")

	line = infile.readline().strip().split()
	min=int(line[0])
	max=int(line[1])
	count=0

	for attempt in range(math.ceil(math.sqrt(min)), math.floor(math.sqrt(max)+1)):
		if isPalindrome(attempt):
			if isPalindrome(attempt*attempt):
				count+=1
	print(count)

