"""
started 06/25/2022

Not completed
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        myd = {}
        for c in t:
            myd[c] = []
        
        for i in range(len(s)):
            mychar = s[i]
            if mychar in myd:
                myd[mychar].append(i)
        
        # reverse each list to make into stacks
        for k, v in myd.items():
            myd[k] = v[::-1]
        
        
        smallest = largest = None
        result = 0
        while 1:

            for k, v in myd.items():
                pass