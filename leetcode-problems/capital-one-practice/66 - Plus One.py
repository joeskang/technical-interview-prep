'''
Runtime: 65 ms, faster than 5.05% of Python3 online submissions for Plus One.
Memory Usage: 14.3 MB, less than 14.13% of Python3 online submissions for Plus One.
'''

# method 1

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        exp = 0
        # output = []
        output = 0
        while digits:
            dig = int(digits.pop())

            # output.append(dig)
            output += dig * 10 ** exp
            exp += 1

        arr = []
        output += 1
        while output > 0:
            arr.insert(0, output % 10)
            output //= 10
        return arr  


