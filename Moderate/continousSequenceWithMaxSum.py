def continousSequenceWithMaxSum(arr):
    # Initialize variables to keep track of the maximum sum and the current sum.
    max_sum = 0
    sum = 0
    
    # Iterate through the elements of the input array 'arr'.
    for i in range(len(arr)):
        # Add the current element 'arr[i]' to the current sum.
        sum += arr[i]
        
        # Compare the current sum with the maximum sum seen so far.
        if sum > max_sum:
            max_sum = sum  # If the current sum is greater, update the maximum sum.
        elif sum < 0:
            sum = 0  # If the current sum becomes negative, reset it to zero.
    
    # Return the maximum sum found in the continuous subarray.
    return max_sum

# Call the function with an example input array.
continousSequenceWithMaxSum([2, -8, 3, -2, 4, -10])

"""The code you provided is used to find the maximum sum of a continuous subarray within the given arr. This problem is often referred to as the "Maximum Subarray Sum" problem and can be solved using Kadane's algorithm. Let's analyze the space and time complexity of the code:

Time Complexity:
The code uses a single loop to iterate through the elements of the input array arr. In each iteration, it performs a constant amount of work, which includes addition, comparison, and assignment operations. Therefore, the time complexity is O(n), where 'n' is the length of the input array arr.

Space Complexity:
The code uses a constant amount of additional space regardless of the size of the input array. It maintains only a few variables (max_sum, sum, and i), and the space used is not dependent on the size of the input. Therefore, the space complexity is O(1), which means it has constant space complexity.

In summary:

Time Complexity: O(n)
Space Complexity: O(1)"""