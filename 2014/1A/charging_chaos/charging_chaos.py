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
        n, length = infile.readline()
        flows = infile.readline()
        devices = infile.readline()

        flips = 0
        while sorted(flows) != sorted(devices):
            for flow in flows:
                for bit in flow:
                    bit = not bit

        print 'NOT POSSIBLE'

if __name__ == "__main__":
    main()
