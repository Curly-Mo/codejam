#!/usr/bin/env python
import fileinput
import sys


def arrangeBoard(rows, cols, mines):
    board = [['.' for x in xrange(cols)] for x in xrange(rows)] 

    return board


def main():

    infile = fileinput.input()
    numCases = int(infile.readline())
    for case in range(1, numCases+1):
        sys.stdout.write("Case #{}: ".format(case))
        numBlocks = int(infile.readline())
        naomiBlocks = [float(x) for x in infile.readline().strip().split()]
        kenBlocks = [float(x) for x in infile.readline().strip().split()]

        print naomiBlocks
        print kenBlocks

if __name__ == "__main__":
    main()
