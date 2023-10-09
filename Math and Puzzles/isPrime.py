def primeNaive(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
    

def primeSlightlyBetter(n):
    if n<2:
        return False
    sqrt = n**0.5
    for i in range(2,int(sqrt)):
        if n%i==0:
            return False
    return True
    

import time

start = time.time()
print(primeNaive(1000000000000000000))
end = time.time()
print("Prime Naive:",end - start)


start = time.time()
print(primeSlightlyBetter(1000000000000000000))
end = time.time()
print("Prime Slightly Better:",end - start)