import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Write your code here
    if n == 1:
        return n
    elif n == 0:
        return 1
    else:
        return n*factorial(n-1)

num = int(input())
if num >=1:
    print(factorial(num))
    
