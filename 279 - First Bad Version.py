"""
Runtime: 28 ms, faster than 81.69% of Python3 online submissions for First Bad Version.
Memory Usage: 14.3 MB, less than 11.21% of Python3 online submissions for First Bad Version.
"""
BADVERSION = 8

def isBadVersion(num):
    return num >= BADVERSION

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        # binary search seems ideal
        left, right = 0, n
        while left < right:
            pivot = left + (right - left) // 2

            # if the current pivot is bad, then
            if isBadVersion(pivot):
                if not isBadVersion(pivot - 1):
                    return pivot
                # go with first half
                right = pivot - 1
            else:
                left = pivot + 1
        return right

if __name__ == "__main__":
    sol = Solution()
    print(sol.firstBadVersion(20))