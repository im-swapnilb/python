# Python program for practical application of sqrt() function

# import math module
import testMathFunc


# function to check if prime or not
def check(n):
    if n == 1:
        return False

    # from 1 to sqrt(n)
    for x in range(2, (int)(testMathFunc.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True


# driver code
n = 6
if check(n):
    print("prime")
else:
    print("not prime")
