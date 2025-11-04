class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
    
        # Iterate through the list with index and value
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement of the current number exists in the dictionary
            if complement in seen:
                return [seen[complement], i]  # Return the indices of the two numbers
            
            # If not found, store the current number with its index
            seen[num] = i
        
        # Since the problem guarantees exactly one solution, we won't reach here
        return []