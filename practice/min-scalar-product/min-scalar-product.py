import fileinput
import sys


def min_scalar_product(v1, v2):
	return sum([int(x) * int(y) for x, y in zip(sorted(v1), sorted(v2, reverse=True))])

infile=fileinput.input()
numCases=infile.readline()
case=0
while True:
   line1 = infile.readline()
   line2 = infile.readline()
   line3 = infile.readline()
   if not line3: break  # EOF
   case += 1
   sys.stdout.write("Case #"+str(case)+": ")

   list1 = line2.split()
   list2 = line3.split()
   list1 = map(int, list1)
   list2 = map(int, list2)
   print(min_scalar_product(list1,list2))
