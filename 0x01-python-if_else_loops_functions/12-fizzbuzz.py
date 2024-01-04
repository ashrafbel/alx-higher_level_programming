#!/usr/bin/python3
def fizzbuzz():
    for K in range(1, 101):
        if K % 3 == 0 and K % 5 == 0:
            print("FizzBuzz ", end="")
        elif K % 3 == 0:
            print("Fizz ", end="")
        elif K % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(K), end="")
