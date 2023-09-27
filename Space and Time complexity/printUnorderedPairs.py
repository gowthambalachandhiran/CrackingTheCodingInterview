def printUnorderedPairs(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            print(i," ",j)

printUnorderedPairs([1,2,3,4,5])

## Couning the iteration
## We can figure out the runtime by thinking about the what the code "means". It iterates through each pair of values (i,j) where j is bigger then id
## there are n squared total pairs where half of the time i > j and half the other way around. This code rounghly takes N ^ 2 /2 pairs so it does O(N^2)