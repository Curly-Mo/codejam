import fileinput
import sys
import math

def rotate(word):
    return  word[-1:] + word[:-1] 

def getWinner(board,dimension,numToWin):
	redWin = False
	blueWin = False
	for row in board:
		if 'R'*numToWin in row:
			redWin = True
		if 'B'*numToWin in row:
			blueWin = True
	for y in range(0,dimension):
		col = ''.join([q for q in [board[x][y] for x in range(0,dimension)]])
		if 'R'*numToWin in col:
			redWin = True
		if 'B'*numToWin in col:
			blueWin = True
	for y in range(0,dimension):
		diag1 = ''.join([q for q in [board[x][y+x] for x in range(0,dimension-y)]])
		diag2 = ''.join([q for q in [board[x][y-x] for x in range(0,y)]])
		
		if 'R'*numToWin in diag1 or 'R'*numToWin in diag2:
			redWin = True
		if 'B'*numToWin in diag1 or 'B'*numToWin in diag2:
			blueWin = True
	for x in range(0,dimension):
		diag1 = ''.join([q for q in [board[x+y][y] for y in range(0,dimension-x)]])
		diag2 = ''.join([q for q in [board[x+y][dimension-1-y] for y in range(0,dimension-x)]])
		if 'R'*numToWin in diag1 or 'R'*numToWin in diag2:
			redWin = True
		if 'B'*numToWin in diag1 or 'B'*numToWin in diag2:
			blueWin = True

	if redWin and blueWin:
		return "Both"
	if redWin:
		return "Red"
	if blueWin:
		return "Blue"
	return "Neither"

infile=fileinput.input()
numCases=int(infile.readline())

board = [[0 for x in range(4)] for x in range(4)] 
for case in range(1,numCases+1):
	sys.stdout.write("Case #"+str(case)+": ")

	line = infile.readline().strip().split()

	dimension=int(line[0])
	numToWin=int(line[1])
	board=[]

	for x in range(0,dimension):
		row=infile.readline().strip()
		row = row.replace('.','')
		diff = dimension - len(row)
		row = '.'*diff + row
		board.append(row)


	print(getWinner(board,dimension,numToWin))

