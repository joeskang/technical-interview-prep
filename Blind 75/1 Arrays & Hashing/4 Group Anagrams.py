"""
previously completed, redone

time: 00:06:36
date: 10/14/2022
https://leetcode.com/problems/group-anagrams/submissions/

Runtime: 99 ms, faster than 96.80% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.3 MB, less than 80.50% of Python3 online submissions for Group Anagrams.
"""

from collections import defaultdict

def main(strs):
    myd = defaultdict(list)
    # keys: sorted values
    # values: original values

    for s in strs:
        myd[''.join(sorted(s))].append(s)

    return list(myd.values())

if __name__ == "__main__":
    main(['tea', 'ate', 'ant'])
