
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    n = len(a)
    swaps = 0
    for i in range(n-1):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swaps +=1
        
    sorted(a)
    print('Array is sorted in ' +str(swaps) +' swaps.')
    print('First Element: ' +str(a[0]))
    print('Last Element: ' +str(a[n-1]))