import math
def lengthOfLongestSubstring(s: str) -> int:

    left = right = 0
    result = -math.inf
    character_set = set()

    while right < len(s):
        right_char = s[right]
        if right_char not in character_set:
            character_set.add(right_char)
            right += 1
            result = max(result, right - left)
            continue

        while right_char in character_set:
            character_set.remove(s[left])
            left += 1

    return result

def test1():
    s = "abcabcbb"
    assert lengthOfLongestSubstring(s) == 3

def test2():
    s = "bbbb"
    assert lengthOfLongestSubstring(s) == 1

if __name__ == "__main__":
    test1()
    test2()