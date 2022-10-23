"""

This was the first attempt and I had to view a solution

Runtime: 5355 ms, faster than 15.89% of Python3 online submissions for Longest Consecutive Sequence.
Memory Usage: 28.7 MB, less than 87.58% of Python3 online submissions for Longest Consecutive Sequence.

date: 10/23/2022
"""

def longestConsecutive( nums):

    # create a set for fast check if exists
    num_set = set(nums)

    max_length = 0

    # iterate through the nums
    for num in nums:
        # check if we're at the leftmost bound for a group
        if num - 1 not in num_set:
            current_length = 0

            while num in num_set:
                current_length += 1
                num += 1

            max_length = max(max_length, current_length)

    return max_length

def test_solution():
    myarr = [1,100,200,2,3,4,300,500]
    assert longestConsecutive(myarr) == 4

if __name__ == "__main__":
    test_solution()
