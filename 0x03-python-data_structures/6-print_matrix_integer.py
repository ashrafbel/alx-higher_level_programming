#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for x in range(len(row)):
                print("{:d}".format(row[x]), end="\n" if x == len(row) - 1 else " ")
        print()
