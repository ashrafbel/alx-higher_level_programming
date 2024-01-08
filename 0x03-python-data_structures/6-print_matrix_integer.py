#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for x in range(len(row)):
                end_char = "\n" if x == len(row) - 1 else " "
                print("{:d}".format(row[x]), end=end_char)
    else:
        return None
