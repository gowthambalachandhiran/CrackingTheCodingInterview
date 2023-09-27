def printPairs(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(str(i)+" "+str(j))
    
    
## Since inner loop had O(N) iteration and it is called N times. Therefore , the runtime O(N^2). 
##Another way we can see this is by inspection what the "meaning" of the code is. It is printing all pairs (two element sequences).
## There are O(N^2) pairs; therefore the runtime is O(n^2)

printPairs([1,2,3,4,5])