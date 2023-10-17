# 
"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well. You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
# Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 
# Constraints:
0 <= x <= 231 - 1
"""
# Solution
class Solution(object):
    def mySqrt(self, x):
        if x == 0:         # Check if x is 0, in which case the square root is also 0
            return 0
        
        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2 # Calculate the middle value
            if mid * mid == x: # Check if the square of the middle value is equal to x
                return mid
            elif mid * mid < x: # If the square of the middle value is less than x, move the left pointer
                left = mid + 1
            else: # If the square of the middle value is greater than x, move the right pointer
                right = mid - 1
        
        return left - 1 # When the while loop ends, left will be the integer square root rounded down
