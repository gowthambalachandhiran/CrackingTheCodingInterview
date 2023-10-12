def mergeSort(arr):
    # Base case: if the input array has 1 or fewer elements, it is already sorted.
    if len(arr) <= 1:
        return 

    # Calculate the middle index of the array.
    mid = len(arr) // 2

    # Split the array into two halves.
    left = arr[:mid]
    right = arr[mid:]

    # Recursively call mergeSort on the left and right halves.
    mergeSort(left)
    mergeSort(right)

    # Merge the sorted left and right halves.
    mergeSortedArray(left, right, arr)

def mergeSortedArray(left, right, arr):
    i = j = k = 0

    # Merge the left and right arrays into the original array.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Append any remaining elements from the left and right arrays.
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5]
    ]

    for arr in test_cases:
        mergeSort(arr)  # Sort the current test case array using mergeSort.
        print(arr)  # Print the sorted array.

