
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_chars = {}
        for c in s1:
            if c not in s1_chars.keys():
                s1_chars[c] = 1
            else:
                s1_chars[c] += 1

        left = 0
        active = False
        temp = dict(s1_chars)

        for i in range(len(s2)):
            char = s2[i]

            if char in temp and temp[char] > 0:
                if not active:
                    left = i
                    active = True
                    temp[char] -= 1
                    continue

                elif i - left < len(s1):
                    continue

                elif i - left == len(s1):
                    if temp[char] == 1:
                        # winning sequence
                        return True
                else:


            # was going good but hit roadbump, add the first char to temp and set active off
            elif active:
                temp[s2[left]] += 1

            active = False
            # temp = dict(s1_chars)

            # if active

        return False


def test_solution():
    sol = Solution()
    # assert sol.checkInclusion("ab", "eidbaooo")
    # assert not sol.checkInclusion("ab", "eidboaoo")
    assert sol.checkInclusion("adc", "dcda")



