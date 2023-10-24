def minDifference(arr1,arr2):
    arr1.sort()
    arr2.sort()
    i = 0
    j = 0
    difference = float('inf')
    while i < len(arr1) and j < len(arr2):
        if abs(arr1[i]-arr2[j])<difference:
            difference = abs(arr1[i]-arr2[j])
            
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    
    return difference
    

print(minDifference([1,3,15,11,2],[23,18,127,235,19,8]))

"""This algorithm takes O(A log A + B log B) time to sort and O(A+B) time to find the minimum difference. Thereofore overall runtime is O(A log A + B log B)"""
