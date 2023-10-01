class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        z = 0 # XOR variable
        for i in range(len(nums)):
            z = z^nums[i]
        return z