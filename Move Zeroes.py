# 283: Move Zeroes
"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

# Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

# Example 2:
Input: nums = [0]
Output: [0]

# Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

# Follow up: Could you minimize the total number of operations done?
"""
# Solution 1: Using List Comprehension
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Create a new list with all non-zero elements followed by zeros
        nums[:] = [x for x in nums if x != 0] + [0] * nums.count(0)
        
        
# Solution 2: Using a Separate List
class Solution:
    def moveZeroes(self, nums):
        # Separate non-zero and zero elements into two lists
        non_zeros = [x for x in nums if x != 0]
        zeros = [0] * (len(nums) - len(non_zeros))
        # Update the original list with non-zero elements followed by zeros
        nums[:] = non_zeros + zeros


# Solution 3: Using a Loop
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_count = 0

        # Iterate through the list, moving non-zero elements to the left
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                nums[i - zero_count] = nums[i]

        # Fill the end of the list with zeros
        for i in range(len(nums) - zero_count, len(nums)):
            nums[i] = 0