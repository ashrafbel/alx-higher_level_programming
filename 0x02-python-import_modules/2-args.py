#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    C = len(sys.argv) - 1
    if C == 0:
        print("0 arguments.")
    elif C == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(C))
    for X in range(C):
        print("{}: {}".format(X + 1, sys.argv[X + 1]))
