
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # s1 is the smaller string
        # get all the chars of s1
        # dict where key = alpha, val = count
        s1_chars = {}
        for c in s1:
            if c not in s1_chars.keys():
                s1_chars[c] = 1
            else:
                s1_chars[c] += 1

        """only needing to return bool"""
        # indices of chars that are not present in s1
        # indices = []
        # for i in range(len(s2)):
        #     c = s2[i]
        #     if c not in s1_chars:
        #         indices.append(i)
        #
        # suffix = []
        # left = right = 0
        # for ind in range(len(indices)):
        #     copy = dict(s1_chars)
        #     left, right = right + 1, indices[ind]
        #     substring = ''
        #     while left < right:
        #         char = s2[left]
        #         if copy[char]:
        #             copy[char] -= 1
        #             substring += char
        #         else:
        #             suffix.append(substring)
        #             break
        #

        left = right = 0
        copy = dict(s1_chars)
        substring = ''

        while right < len(s2):
            char = s2[right]
            # check to see if haven't depleted chars
            if char in copy:
                if copy[char]:
                    copy[char] -= 1
                    substring += char
                elif len(s1) == len(substring):
                    return True
                else:
                    # restart
                    substring = ''
                    copy = dict(s1_chars)
                    left += 1
                    right = left
                    continue

            else:
                # restart
                substring = ''
                copy = dict(s1_chars)
                left += 1
                right = left
                continue

            if len(s1) == len(substring):
                return True
            right += 1

        return False



def test_solution():
    sol = Solution()
    assert sol.checkInclusion("ab", "eidbaooo")
    assert not sol.checkInclusion("ab", "eidboaoo")
    assert sol.checkInclusion("adc", "dcda")



