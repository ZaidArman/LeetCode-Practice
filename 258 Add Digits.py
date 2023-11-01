# 258: Add Digits
"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

# Example 2:
Input: num = 0
Output: 0

Constraints:
0 <= num <= 231 - 1

# Follow up: Could you do it without any loop/recursion in O(1) runtime?
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Solving Using Digital Root Formula
        # DigitalRoot(num) = 1 + ((num - 1) % 9)
        # Check if the input number is zero. If it is, the digital root is also zero.
        if num == 0:
            return 0
        
        # Check if the number is divisible by 9. If it is, the digital root is 9.
        if num % 9 == 0:
            return 9

        # Calculate the digital root using the formula num % 9.
        return num % 9