def binarySearch(arr, low, high, target):
    mid = (low + high) // 2  # Calculate the middle index of the current search range.
    
    while low <= high:  # While the search range is valid (not empty).
        if target == arr[mid]:  # If the middle element is the target.
            return "Found the element:", target  # Return a message indicating the element is found.

        if target < arr[mid]:  # If the target is less than the middle element.
            high = mid - 1  # Adjust the "high" index to search the left half of the range.
            return binarySearch(arr, low, high, target)  # Recursively search the left half.
        else:  # If the target is greater than the middle element.
            low = mid + 1  # Adjust the "low" index to search the right half of the range.
            return binarySearch(arr, low, high, target)  # Recursively search the right half.
    
    return "Element not found"  # If the loop completes without finding the element, return a "not found" message.

arr = [1, 2, 3, 4, 5]  # Input array.
print(binarySearch(arr, 0, len(arr) - 1, 4))  # Call the binary search function for target 4 and print the result.
print("\n")  # Print a newline for separation.
print(binarySearch(arr, 0, len(arr) - 1, 6))  # Call the binary search function for target 6 and print the result.
