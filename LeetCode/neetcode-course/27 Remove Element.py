
"""
Runtime: 66 ms, faster than 40.48% of Python3 online submissions for Remove Element.
Memory Usage: 13.9 MB, less than 14.39% of Python3 online submissions for Remove Element.
"""

def solution(nums: list, val: int):

    cur_index = count = 0
    for i, num in enumerate(nums):
        if num != val:
            nums[cur_index] = num
            cur_index += 1
            count += 1
        if i > cur_index:
            nums[i] = None
    return count