"""
Runtime: 1001 ms, faster than 5.84% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.3 MB, less than 55.84% of Python3 online submissions for Longest Substring Without Repeating Characters.

Time: 18m 45s (12/7/2021)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest_count = 0
        index = 0
        # initial attempt of brute force

        for left in range(len(s)):
            cur = left
            mys = {}  # keys: char, vals: indices

            # put leftmost in dict
            mys[s[left]] = left
            count = 1

            while cur < len(s) - 1:
                cur += 1
                new_char = s[cur]

                if new_char not in mys.keys():
                    mys[new_char] = cur
                    count += 1

                else:
                    break

            if count > longest_count:
                longest_count = count
                index = left

        return longest_count


def test_solution():
    sol = Solution()
    assert sol.lengthOfLongestSubstring("abcabcabc") == 3
    assert sol.lengthOfLongestSubstring("bbbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3

