"""
decent problem

06/25/2022
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        myd = {}
        
        for s in strs:
            
            myl = [c for c in s]
            myl.sort()
            new_s = "".join(myl)
            if new_s not in myd:
                myd[new_s] = [s]
            else:
                myd[new_s] += [s]
            
        results = []
        for val in myd.values():
            results += [val]
            
        return results