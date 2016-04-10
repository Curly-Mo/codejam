import fileinput
import sys
import math
import itertools
import functools


def makeGuess(facts, product, n):
	guess=""
	multipleFacts=[]
	for x in range(0,n):
		multipleFacts.append(facts)
	permutations = list(itertools.product(*multipleFacts))
	for permute in permutations:
		if functools.reduce(lambda x, y: x*y, permute) == product:
			for num in permute:
				guess+=str(num)
			return guess	
	return guess

def factors(n):
    return set(x for tup in ([i, n//i] 
                for i in range(1, int(n*0.5)+1) if n % i == 0) for x in tup)

infile=fileinput.input()
numCases=int(infile.readline())

for case in range(1,numCases+1):
	print("Case #"+str(case)+": ")

	line1 = infile.readline().strip().split()
	
	R=int(line1[0])
	N=int(line1[1])
	M=int(line1[2])
	K=int(line1[2])
	

	for i in range (0,R):
		guess=""
		products = infile.readline().strip().split()
		products=[int(x) for x in products]
		allFactors = []
		for product in products:
			facts = factors(product)
			facts = [s for s in facts if s <= M and s >= 2]
			if len(facts) == N:
				count=N
				while len(guess)<N and count>1:
					guess+=makeGuess(facts, product, count)
					count -= 1
		for product in products:
			facts = factors(product)
			facts = [s for s in facts if s <= M and s >= 2]
			allFactors.append(facts)
			count=N
			while len(guess)<N and count>1:
				guess+=makeGuess(facts, product, count)
				count -= 1

		allFactors = sorted(allFactors, key=len)
		if len(guess)<N:
			for facts in allFactors:
				for num in facts:
					if len(guess)<N:
						guess+=str(num)
		while len(guess)<N:
			guess+="2"
		print(guess[0:N])

	

