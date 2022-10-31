"""
I have previously solved this problem multiple times. Redoing to refresh my memory

time: 00:03:56
date: 10/13/2022
https://leetcode.com/problems/contains-duplicate/
"""

def main(nums: list):
    myset = set()
    for num in nums:
        if num in myset:
            return True
        myset.add(num)

    return False

if __name__ == "__main__":
    nums = [1,1,1,2,4,5]
    assert main(nums)
    assert not main([])
    assert not main([1,2,3])