import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    biner = []
    while n>0:
        x = n%2
        n = n//2
        biner.append(x)
        
    count = 0
    result = 0
    
    for i in range(0,len(biner)):
        if biner[i] == 1:
            count +=1
            result = max(result,count)
        elif biner[i] == 0:
            count = 0
    print(result)