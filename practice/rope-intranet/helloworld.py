import fileinput
import sys


def min_scalar_product(v1, v2):
	return sum([int(x) * int(y) for x, y in zip(sorted(v1), sorted(v2, reverse=True))])

infile=fileinput.input()
numCases=int(infile.readline())

for case in range(1,numCases+1):
   sys.stdout.write("Case #"+str(case)+": ")
   numWires = int(infile.readline())
   wires=[]
   for wire in range(0,numWires):
      wire=infile.readline().split()
      wire = [ int(x) for x in wire ]
      wires.append(wire)

   intersections=0
   for x in range(0,numWires):
      for y in range(x+1, numWires):
         if(wires[x][0]<wires[y][0] and wires[x][1]>wires[y][1] or wires[x][0]>wires[y][0] and wires[x][1]<wires[y][1]):
            intersections += 1

   print(intersections)


