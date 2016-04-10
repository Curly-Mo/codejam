import fileinput
import sys
import re


infile=fileinput.input()
firstLine=infile.readline().split()
numLetters=int(firstLine[0])
numWords=int(firstLine[1])
numCases=int(firstLine[2])

dictionary = "".join(infile.readline() for i in range(numWords))


case=0
while True:
   line = infile.readline()
   if not line: break  # EOF
   case += 1
   sys.stdout.write("Case #"+str(case)+": ")

   word = line.replace("(", "[")
   word = word.replace(")", "]")
   print(len(re.findall(word, dictionary)))
   
