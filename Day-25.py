from math import sqrt

n = int(input())

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

for i in range(n):
    num = int(input())
    
    if num >= 2 and isPrime(num):
        print('Prime')
    else:
        print('Not prime')