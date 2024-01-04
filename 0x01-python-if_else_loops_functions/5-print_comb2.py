#!/usr/bin/python3
for K in range(100):
    if K < 99:
        print("{:02d}, ".format(K), end="")
    else:
        print("{:02d}".format(K))
