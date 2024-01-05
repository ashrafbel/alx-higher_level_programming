#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    S = 0
    for X in range(len(sys.argv) - 1):
        S += int(sys.argv[X + 1])
    
    print(S)
