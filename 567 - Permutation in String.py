
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # s1 is the smaller string
        # get all the chars of s1
        # dict where key = alpha, val = count
        # s1_chars = {}
        # for c in s1:
        #     if c not in s1_chars.keys():
        #         s1_chars[c] = 1
        #     else:
        #         s1_chars[c] += 1
        #
        #
        # left = right = 0
        # copy = dict(s1_chars)
        # substring = ''
        #
        # while right < len(s2):
        #     char = s2[right]
        #     # check to see if haven't depleted chars
        #     if char in copy:
        #         if copy[char]:
        #             copy[char] -= 1
        #             substring += char
        #         elif len(s1) == len(substring):
        #             return True
        #         else:
        #             # restart
        #             substring = ''
        #             copy = dict(s1_chars)
        #             left += 1
        #             right = left
        #             continue
        #
        #     else:
        #         # restart
        #         substring = ''
        #         copy = dict(s1_chars)
        #         left += 1
        #         right = left
        #         continue
        #
        #     if len(s1) == len(substring):
        #         return True
        #     right += 1
        #
        # return False

        # make a dict for the first string's characters
        s1_dict = {}
        for c in s1:
            if c not in s1_dict:
                s1_dict[c] = 0
            else:
                s1_dict[c] += 1

        for i in range(len(s2) - 3):
            first_char = s2[i]
            last_char






def test_solution():
    sol = Solution()
    assert sol.checkInclusion("ab", "eidbaooo")
    assert not sol.checkInclusion("ab", "eidboaoo")
    assert sol.checkInclusion("adc", "dcda")



