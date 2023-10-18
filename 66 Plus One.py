# Plus One
"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's. Increment the large integer by one and return the resulting array of digits.

# Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

# Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

# Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

# Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""

#Solution:

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        result = []

        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry # Calculate the sum of the current digit, carry, and 1
            carry = total // 10 # Calculate the new carry value for the next iteration
            # result.insert(0, total % 10) # Update the current digit in the result
            result = [total % 10] + result
        if carry > 0: # If there's a carry left after processing all digits, add it to the result
            # result.insert(0, carry)
            result = [carry] + result
        return result