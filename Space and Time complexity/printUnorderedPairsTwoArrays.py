def printUnorderedPairsTwoArrays(list1,list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            print(i," ",j)
            

printUnorderedPairsTwoArrays([1,2,3,4],[6,7])

##for each element of list1,the inner for loop goes through list2 iterations,where 1st loop will run first length and 2nd loop will run length of second list2
##it is O(list1*list2) instead of O(N^2)