import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []
    maximum = -9*6

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i+2<6 and j+2<6:
                result = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
                if result > maximum:
                    maximum = result
    print(maximum)
