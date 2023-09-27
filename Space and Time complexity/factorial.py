def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
        
### This follows n-1,n-2,n-2.......till 1

### Since we go till N in reverse till 1 this is O(n)

print(factorial(5))