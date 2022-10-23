"""
INITIALLY MISREAD THE PROBLEM. THE FOLLOWING IS ROMAN TO INT:

class Solution:
    def intToRoman(self, num: int) -> str:
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
            if k in num:
                num = num.replace(k, '')
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
        
        for n in num:
            total += numerals[n]
            
        return total
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        
        result = ""
        

        
        numerals = [
            ("M", 1000),
            ("D", 500),
            ("C", 100),
            ("L", 50),
            ("X", 10),
            ("V", 5),
            ("I", 1)
        ]
        numerals = numerals[::-1]

        
        exceptions = [
            ("CM", 900),
            ("CD", 400),
            ("XC", 90),
            ("XL", 40),
            ("IX", 9),
            ("IV", 4)
        ]
        exceptions = exceptions[::-1]
        
        n_key, n_val = numerals.pop()
        e_key, e_val = exceptions.pop()
        
        while num:
            if num >= n_val:
                num -= n_val
                result += n_key
            elif num >= e_val:
                num -= e_val
                result += e_key
            else:
                if len(numerals) == 0:
                    break
                n_key, n_val = numerals.pop()
                if len(exceptions) > 0:
                    e_key, e_val = exceptions.pop()
                
        return result
                
                
                
