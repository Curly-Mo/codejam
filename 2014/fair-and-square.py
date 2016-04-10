import fileinput


def main():

    infile = fileinput.input()
    numCases = int(infile.readline())

    for case in range(1, numCases+1):
        print "Case #{}: ".format(case)
        line = infile.readline().strip().split()

if __name__ == "__main__":
    main()
