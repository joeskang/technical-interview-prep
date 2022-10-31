"""
Had previously completed. Review

time: 00:02:50
date: 10/14/2022
https://leetcode.com/problems/valid-anagram/submissions/
"""


def isAnagram(self, s: str, t: str) -> bool:
    # edge case
    if len(s) != len(t):
        return False
    if len(s) == len(t) == 0:
        return True

    s, t = sorted(s), sorted(t)

    return s == t


