"""
Runtime: 54 ms, faster than 88.46% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14.4 MB, less than 85.48% of Python3 online submissions for Valid Palindrome.

date: 10/23/2022
time: 00:09:11
"""

def isPalindrome(s:str):

    # need to make lowercase and remove all non-alpha

    s = s.lower()
    left, right = 0, len(s) - 1
    while left < right:
        # check if left is alpha
        if not (s[left].isalpha() or s[left].isnumeric()):
            left += 1
        elif not (s[right].isalpha() or s[right].isnumeric()):
            right -= 1
        else:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
    return True
