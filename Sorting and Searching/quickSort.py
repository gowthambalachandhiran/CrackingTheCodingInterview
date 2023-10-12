def quickSort(arr):
    
    if len(arr)<=1:
        return 
    pivot = arr[0]
    left, equal, right = [], [], []
    
    for element in arr:
        if element < pivot:
            left.append(element)
        if element > pivot:
            right.append(element)
        if element == pivot:
            equal.append(element)
    # Recursively sort the left and right partitions.
    sorted_left = quickSort(left)
    sorted_right = quickSort(right)
    
    return left+equal+right
    
  
if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5]
    ]

    for arr in test_cases:
        sorted_arr = quickSort(arr)  # Sort the current test case array using Quick Sort.
        print(sorted_arr)