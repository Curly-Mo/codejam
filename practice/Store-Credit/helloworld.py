import fileinput
import sys


def getIndicesThatSumTo(sum,numValues,values):
   for x in range(0, numValues):
      item1=values[x]
      for y in range(x+1, numValues):
         item2=values[y]
         if int(item1) + int(item2) == sum:
            print(str(x+1) + " " + str(y+1))
            return


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

   getIndicesThatSumTo(int(line1),int(line2),line3.split())