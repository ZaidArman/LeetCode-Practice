# 67 Add Binary: Given two binary strings a and b, return their sum as a binary string.
""" 
# Example 1:
Input: a = "11", b = "1"
Output: "100"

# Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

# Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

class Solution(object):
    def addBinary(self, a, b):
        # Approach I: Convert binary strings to integers, add them, and convert back to binary
        # Convert the binary strings 'a' and 'b' to integers, add them, and convert the result back to binary format.
        result = bin(int(a, 2) + int(b, 2))[2:]

        # Approach II: Binary addition without conversion to integers
        # This approach directly adds binary strings without converting to integers.
        # Ensure both binary strings have the same length by padding with leading zeros.
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        carry = 0
        result = []

        # Iterate through binary strings from right to left (least significant to most significant bits).
        for i in range(max_len - 1, -1, -1):
            bit_sum = int(a[i]) + int(b[i]) + carry
            carry = bit_sum // 2
            result.append(str(bit_sum % 2))

        # If there is a carry after the loop, add it to the result.
        if carry:
            result.append('1')

        # Return the result as a binary string.
        return ''.join(result[::-1])
