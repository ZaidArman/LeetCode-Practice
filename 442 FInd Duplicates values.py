# LeetCode problem No: 442 
class Solution(object):
    def findDuplicates(self, nums):
        result = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1  # Adjust the index to start from 0
            if nums[index] >= 0:
                nums[index] = -nums[index]
            else:
                result.append(abs(nums[i]))
        return result

# Create an instance of the class
# solution = Solution()

        