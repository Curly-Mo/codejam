#!/usr/bin/env python
import fileinput
import sys


def arrangeBoard(rows, cols, mines):
    board = [['.' for x in xrange(cols)] for x in xrange(rows)]
    for row in xrange(rows):
        for col in xrange(cols):
            if mines > 0:
                board[row][col] = '*'
                mines -= 1

    return board


def main():

    infile = fileinput.input()
    numCases = int(infile.readline())

    for case in range(1, numCases+1):
        sys.stdout.write("Case #{}: ".format(case))
        rows, columns, mines = [int(x) for x in infile.readline().strip().split()]

        board = arrangeBoard(rows, columns, mines)
        print board

if __name__ == "__main__":
    main()
