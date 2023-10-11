class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) # Initialize low and high indices for binary search
        
        while low < high:         # Perform binary search while low is less than high
            mid = low + (high - low) // 2             # Calculate the middle index
            
            # Check if the target is greater than the value at mid
            if target > nums[mid]:
                low = mid + 1 # Update low to mid + 1 to search the right half
            else:
                high = mid# Update high to mid to search the left half

        return low         # Return the low index as the insertion point for the target
