#!/bin/env python3

#from codecs import encode
#cluetext = 'znxr n yvfg bs cevzrf naq fhz gur barf gung ner ng cevzr vaqrkrf'
#encode(cluetext,'rot13')
#Note: In rot13, decode and encode are the same, hence it's popularity~
#Session ID: f73709aed14f45058a7b7e75d46a88c7

import time
from IPython.display import clear_output
import sys

def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    #print(primes)
    return len(primes)


def is_prime(num):
    if num < 2: return False
    if num == 2: return True
    primes=[2]
    x=3
    
    while x <= num:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            if x==num: return True
            x+=2
    #print(primes)
    return False
    
from numba import jit
@jit
def sum_prime_primes(num):
    if num < 2: return 0
    if num == 2: return 2
    primes=[2]
    x=3
    primesum=0
    index=0
    while x <= num:
        #print("X=",x)
        for y in primes:  # use the primes list!
            if x%y == 0:
                #print(x,"is divisible by",y)
                x+=2
                break
        else:
            index+=1
            primes.append(x)
            #print(index,primes)
            if index in primes:
                #print("adding",x,"to primesum")
                primesum+=x
                #clear_output()
                #print("Adding",x,"sum is now",primesum)
            x+=2

    return primesum
 

if __name__ == '__main__':

    limit = 10000
    if len(sys.argv) > 1:
        limit = int(sys.argv[1])

    start = time.time()
    result = sum_prime_primes(limit)
    print("Limit:",limit,"Result:",result)
    end = time.time()
    print(end - start)


# First result
# 5036061511056


