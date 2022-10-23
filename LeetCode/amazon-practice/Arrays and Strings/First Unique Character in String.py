"""
June 26, 2022
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # will just use a dict
        # keys: letters
        # values: index, repeats will have value of None
        myd = {}
        for i in range(len(s)):
            curr = s[i]
            myd[curr] = i if curr not in myd else False

        min_index = len(s)
        for k, v in myd.items():
            if v is False:
                continue
            min_index = min(v, min_index)

        return min_index if min_index < len(s) else -1
