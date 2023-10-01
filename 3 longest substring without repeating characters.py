class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = 0
        current_sub_string = 0
        current_len = 0
        longest_string = 0
        
        for i, letter in enumerate(s):
            if letter in substring and substring[letter] >= current_sub_string:
                current_sub_string = substring[letter] + i
                current_len = i - substring[letter]
                substring = i
            else:
                substring = i
                current_len += 1
                if current_len > longest_string:
                    longest_string = current_len
        return (longest_string)
            
        # Solution 2
        '''charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res'''
