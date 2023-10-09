"""First we create array named flag with size equal to total numbers initializing them to True

then we start with p = 2

while the square of p is less then equal to N go to next step

Check if flag[p] == True go to next step

then we iterate starting with square of p till N with steps p 

mark the index of iteration as False

Increment the p value by one"""

def sieveOfEratosthenes(n):
    p = 2
    flag = [True for i in range(n+1)]
    while p*p <=n:
        if flag[p] == True:
            for i in range(p*p,n+1,p):
                flag[i] = False
                
        p += 1
    return flag
    

flag = sieveOfEratosthenes(120)

for i in range(2,len(flag)):
    if flag[i]:
        print(i,"\n")
        
        