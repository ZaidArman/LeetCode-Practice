# 290. Word Pattern
"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

# Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

# Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

# Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

# Constraints:
1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""

class Solution(object):
    def wordPattern(self, pattern, s):
        # Dictionaries to store the mapping between characters and words
        char_to_word = {}
        word_to_char = {}

        # Tokenize the input string into words
        words = s.split()

        # Check if the length of pattern and number of words match
        if len(pattern) != len(words):
            return False

        # Iterate through each character and word in the pattern and string
        for ch, word in zip(pattern, words):
            # Check for a different word for the same character
            if ch in char_to_word and char_to_word[ch] != word:
                return False  # Different word for the same character

            # Check for a different character for the same word
            if word in word_to_char and word_to_char[word] != ch:
                return False  # Different character for the same word

            # Update the dictionaries with the current character and word
            char_to_word[ch] = word
            word_to_char[word] = ch

        # If all checks pass, return True
        return True
