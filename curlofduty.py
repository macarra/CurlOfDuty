
# coding: utf-8

# In[1]:


## From Whiteboard page
#from codecs import encode
#cluetext = 'znxr n yvfg bs cevzrf naq fhz gur barf gung ner ng cevzr vaqrkrf'
#encode(cluetext,'rot13')
#Note: In rot13, decode and encode are the same, hence it's popularity~
#Session ID: f73709aed14f45058a7b7e75d46a88c7

Result of decode: make a list of primes and sum the ones that are at prime indexes
# In[2]:


import matplotlib.pyplot as P
import time
from IPython.display import clear_output


# In[3]:


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


# In[4]:


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
    


# In[5]:


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
#sum_prime_primes(1034382)


# In[6]:


sum_prime_primes(100)


# ### Result 1
# #sum_prime_primes(50000000)
# 
# 5036061511056

# In[7]:


#elapsed=[]
#for x in range(1000,100000,1000):
#    start = time.time()
#    sum_prime_primes(x)
#    end = time.time()
#    elapsed.append(end-start)
#print(elapsed)

