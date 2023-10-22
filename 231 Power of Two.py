# Problem # 231: Power of Two
"""
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

# Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

# Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

# Example 3:
Input: n = 3
Output: false
 

# Constraints:
-231 <= n <= 231 - 1

# Follow up: Could you solve it without loops/recursion?
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Sulotion 1: Using loop
        if n <= 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1

        # Follow up: Could you solve it without loops/recursion?

        # Solution 2: Using Bit Manipulation
        if n <= 0:
            return False
        return n & (n - 1) == 0
                # OR    
        return n > 0 and n & (n - 1) == 0       
