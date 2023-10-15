class Solution(object):
    def countPrefixes(self, words, s):
        
        count = 0  # Initialize a counter to keep track of the number of matching prefixes.
        
        for word in words:
            if s.startswith(word):  # Check if the string s starts with the current word.
                count += 1  # If it does, increment the count.

        return count