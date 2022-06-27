"""
date: 6/25/2022
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        exceptions = {
            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4
        }
        total = 0
        for k,v in exceptions.items():
            if k in s:
                s = s.replace(k, '')
                total += v
        
        numerals = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1,
        }
        
        for n in s:
            total += numerals[n]
            
        return total