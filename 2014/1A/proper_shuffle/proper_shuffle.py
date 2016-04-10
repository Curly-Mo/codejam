#!/usr/bin/env python
import fileinput
import sys
import random


def good(identity):
    a = list(identity)
    for k in a:
        p = int(round(random.uniform(k, len(a) - 1)))
        a[k], a[p] = a[p], a[k]
    return a


def bad(identity):
    a = list(identity)
    for k in a:
        p = int(round(random.uniform(0, len(a) - 1)))
        a[k], a[p] = a[p], a[k]
    return a


def main():

    infile = fileinput.input()
    numCases = int(infile.readline())

    for case in range(1, numCases+1):
        sys.stdout.write("Case #{}: ".format(case))
        n = int(infile.readline())
        permutation = [int(x) for x in infile.readline().strip().split()]
        identity = range(n)

        good_times = 0
        bad_times = 0
        too_many = 0
        tries = 100
        while((abs(good_times - bad_times) < tries) and too_many < tries*30):
            if good(identity) == permutation:
                good_times += 1
            if bad(identity) == permutation:
                bad_times += 1
            too_many += 1

        print good_times
        print bad_times
        if bad_times > good_times:
            print 'BAD'
        else:
            print 'GOOD'

if __name__ == "__main__":
    main()
