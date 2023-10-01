class Solution(object):
    def majorityElement(self, nums):
# Here the complexity of sort is O(n log n) and complexity of loop is O(n). So the total complexity of the solution is O(n log n) """
        # nums.sort()
        # count = 0
        # n = len(nums)//2 # majority condition
        # number = nums[0] 
        # for i in range(len(nums)):
        #     if number == nums[i]:
        #         count += 1
        #     else:
        #         count = 1
        #     if count > n:
        #         return number
        #     number = nums[i]

# Follow-up: Could you solve the problem in linear time and in O(1) space?
            # Boyer Moore ALgorithm
        count = 0
        m = 0
        for i in range(len(nums)):
            if count == 0:
                m = nums[i]
                count += 1
            else:
                if m == nums[i]:
                    count += 1
                else: 
                    count -= 1
        for i in range(len(nums)):
            if nums[i] == m:
                count += 1
        if count > (len(nums)//2):
            return m