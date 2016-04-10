import fileinput
import sys


infile=fileinput.input()
numCases=infile.readline()
case=0
while True:
   line = infile.readline()
   if not line: break  # EOF
   case += 1
   sys.stdout.write("Case #"+str(case)+": ")

   wordList = line.split()
   wordList.reverse()
   print(' '.join(wordList))
