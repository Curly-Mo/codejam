#!/usr/bin/env python
import fileinput
import sys


def find_card(rows1, rows2, answer1, answer2):
    return set(rows1[answer1]).intersection(set(rows2[answer2]))


def main():

    infile = fileinput.input()
    numCases = int(infile.readline())

    for case in range(1, numCases+1):
        sys.stdout.write("Case #{}: ".format(case))
        numNodes = int(infile.readline())

        tree = [list() for _ in xrange(numNodes)]
        for x in xrange(1, numNodes):
            line = [int(x) for x in infile.readline().strip().split()]
            a, b = line
            a = a - 1
            b = b - 1
            tree[a].append(b)
            tree[b].append(a)

        print tree

if __name__ == "__main__":
    main()
