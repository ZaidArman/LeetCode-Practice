class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        
        digits = 0
        reversed_num = 0
        while(x // (10**digits) != 0):
            reversed_num = reversed_num*10 + (x // (10**digits) % 10)
        return (x == reversed_num)

# solution = Solution()


# Solution 2
# def ispalindrome(x):
#     z = str(x) == str(x)[::-1]
#     return(z)
# x = 10
# print(ispalindrome(x))