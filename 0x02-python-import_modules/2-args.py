#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    C = len(sys.argv) - 1

    if C != 1:
        print("{} arguments:".format(C))
        for X in range(C):
            print("{}: {}".format(X + 1, sys.argv[X + 1]))
    elif C == 0:
        print("0 arguments.")
    else:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))

