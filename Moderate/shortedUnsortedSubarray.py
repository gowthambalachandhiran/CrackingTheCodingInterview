class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1:
            return 0

        left, right = 0, n - 1

        # Find the left index where the array is out of order
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1

        if left == n - 1:
            # The entire array is already sorted
            return 0

        # Find the right index where the array is out of order
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1

        # Find the minimum and maximum elements in the unsorted subarray
        min_val, max_val = min(nums[left:right + 1]), max(nums[left:right + 1])

        # Expand the subarray to the left to include any elements greater than min_val
        while left > 0 and nums[left - 1] > min_val:
            left -= 1

        # Expand the subarray to the right to include any elements smaller than max_val
        while right < n - 1 and nums[right + 1] < max_val:
            right += 1

        return (right-left)+1


# Example usage with a new test case:
nums = [1, 3, 5, 2, 6, 4, 8]
result = find_unsorted_subarray(nums)
print(result)  # Output: [1, 5]

