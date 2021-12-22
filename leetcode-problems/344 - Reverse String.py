"""
Runtime: 208 ms, faster than 40.46% of Python3 online submissions for Reverse String.
Memory Usage: 18.5 MB, less than 62.51% of Python3 online submissions for Reverse String.

Time: 4m 13s (12/7/2021)
"""
class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        for i in range(len(s)//2):
            s[i], s[-1 - i] = s[-1 - i], s[i]


        # for debugging
        return s


def test_solution():
    sol = Solution()
    assert sol.reverseString(['h','e','l','l','o']) == ['o','l','l','e','h']
    assert sol.reverseString(['a','b','c','d','e','f']) == ['f','e','d','c','b','a']

if __name__ == "__main__":
    test_solution()