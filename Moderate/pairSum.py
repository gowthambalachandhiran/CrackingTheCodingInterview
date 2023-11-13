def twoSum(self, nums: List[int], target: int) -> List[int]:
	num_indices = {}  # Dictionary to store the complement and its index

	for index, num in enumerate(nums):
		complement = target - num
		if complement in num_indices:
			return [num_indices[complement], index]
		num_indices[num] = index