def reverse(array):
    print(array,"\n")
    for i in range(len(array)//2):
        other  = len(array)-i-1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
        
    print(array)
    
reverse([1,2,3,4,5,6,7,8])

##Thus algorithm runs in  O(N) time . The fact that it only goes through half of the array (in terms of iterations) does not impact the big O time.