"""
decent

Date: 06/25/2022
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) < 3:
            return result
        
        nums.sort()
        myd = {}
        
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            # filter out all positives or all negatives
            
                
            while k > j:
                l, m, r = nums[i], nums[j], nums[k]
                if (l < 0 and m < 0 and r < 0) or (l > 0 and m > 0 and r > 0):
                    break
                if (sum_ := l + m + r) > 0:
                    k -= 1
                elif sum_ < 0:
                    j += 1
                else:
                    myd[(l, m)] = r
                    j += 1
                
        for k, v in myd.items():
            result += [[k[0], k[1], v]]
        return result
                