# Dictionary to store computed Fibonacci numbers
fib_dict = {}

def fibonacci(n):
    # Check if the Fibonacci number for n is already computed
    if n in fib_dict:
        return fib_dict[n]
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive calculation and memoization
    fib_value = fibonacci(n-1) + fibonacci(n-2)
    fib_dict[n] = fib_value
    return fib_value

# Generate the Fibonacci sequence up to a certain number, e.g., 10
n = 10
fib_sequence = [fibonacci(i) for i in range(n+1)]
print(fib_sequence)

## Since we dont compute values recursively if calculated once we store them in dictionary to use later.
## The total time it take for us to complete all the values in O(N)