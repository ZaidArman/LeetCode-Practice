class Solution(object):
    def reverse(self, x):
        # Define the minimum and maximum values for a 32-bit signed integer
        MIN = -2147483648  # Equivalent to -2**31
        MAX = 2147483647   # Equivalent to 2**31 - 1
        
        # Check if the input integer is negative
        is_negative = x < 0
        
        # Take the absolute value of x to work with it without the sign
        x = abs(x)
        
        # Initialize the result to store the reversed integer
        result = 0

        # Reverse the digits of x
        while x != 0:
            # Extract the last digit of x
            last_digit = x % 10
            
            # Build the result by shifting digits and adding the last digit
            result = result * 10 + last_digit
            
            # Remove the last digit from x
            x //= 10

        # Check if the reversed result is within the 32-bit integer range
        if result < MIN or result > MAX:
            return 0
        
        # Restore the original sign if x was negative
        if is_negative:
            result = -result

        # Return the reversed and possibly negated integer
        return result
