def fib(n):
    if n == 0 : return 0
    if n == 1 : return 1
    else:
        return fib(n-1)+fib(n-2)
        
## Since there are two branches the actual calls would be O(2^N)

print(fib(5))