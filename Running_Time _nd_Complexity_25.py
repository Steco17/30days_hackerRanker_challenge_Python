# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

P = int(input())


def isPrime(n):
    for i in range(2, int(sqrt(n)+1)):
        if n % i is 0:
            return False
    return True


for _ in range(P):
    n = int(input())
    
    if n >= 2 and isPrime(n):
        print("Prime")
    else:
        print("Not prime")