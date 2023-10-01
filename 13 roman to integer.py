class Solution:
    def romanToInt(self, s: str) -> int:
        roman_table = {
                    "I": 1, 
                    "V": 5, 
                    "X": 10, 
                    "L": 50, 
                    "C": 100, 
                    "D": 500, 
                    "M": 1000
                }
        
        number = 0
        last_num = 'I'
        
        for num in s[::-1]:
            if roman_table[num] < roman_table[last_num]:
                number -= roman_table[num]
            else:
                number += roman_table[num]
            last_num = num
        return number
        
