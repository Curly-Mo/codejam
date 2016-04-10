import fileinput
import sys


def min_scalar_product(v1, v2):
	return sum([int(x) * int(y) for x, y in zip(sorted(v1), sorted(v2, reverse=True))])

infile=fileinput.input()
numCases=int(infile.readline())
root=set([])

for case in range(1,numCases+1):
   sys.stdout.write("Case #"+str(case)+": ")
   inputs = infile.readline().split()
   print (inputs)
   numExisting = int(inputs[0])
   numAdding = int(inputs[1])

   for path in range(0,numExisting):
      dirs=infile.readline().split('/')
      dirs=set(dirs)
      root.add(dirs)

   for path in range(0,numAdding):
      dirs=infile.readline().split('/')
      


