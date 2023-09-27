def powerOf2(n):
    if n<1:
        return 0
    elif n==1:
        print(1,"\n")
        return 1
    else:
        prey = powerOf2(n//2)
        curr = prey * 2
        print(curr,"\n")
        return curr
        
        
## Since each time we half the call in the recursion call stack it is eventually 0(log N)

powerOf2(1000000)