
class Solution:
    def intToRoman(self, num: int) -> str:

        exponent = 0
        while num:

            digit = num % (10**(exponent + 1))
            num //= (10**exponent)
