"""
Runtime: 104 ms, faster than 14.68% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 15.1 MB, less than 30.15% of Python3 online submissions for Reverse Words in a String III.

Time: 10m 58s (12/7/21)
"""
class Solution:
    def reverseWords(self, s: str) -> str:

        def reverse_chars(ins: str):
            chars = list(c for c in ins)
            for i in range(len(chars)//2):
                chars[i], chars[-1-i] = chars[-1-i], chars[i]
            outp = ''
            for c in chars:
                outp += c
            return outp


        words = s.split()
        # words.reverse()

        output = ""
        for word in words:
            output += reverse_chars(word)
            output += " "

        return output[:-1]


def test_solution():
    sol = Solution()
    assert sol.reverseWords("Hello World") == "olleH dlroW"

if __name__ == "__main__":
    test_solution()
