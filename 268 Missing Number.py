class Solution(object):
    def missingNumber(self, nums):
        # Solution 1
        
        # for i in range(len(nums)):
        #     if i not in nums:
        #         return i

        # Solution 2
        a = 0
        b = 0
        for i in range(len(nums) + 1):
            a = a ^ i
        for i in range(len(nums)):
            b = b ^ nums[i]
        
        return a^b