def isPrime(n):
    x = 2
    while x*x <= n:
        if (n%x == 0):
            print("Not a prime")
            return 
        x += 1
    print("Prime")
    return 
    

isPrime(51)