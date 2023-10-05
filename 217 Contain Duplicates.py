class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ZeeSet = set()

        for n in nums:
            if n in ZeeSet:
                return True
            ZeeSet.add(n)
        return False
        