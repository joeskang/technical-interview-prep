"""
June 26, 2022
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # two different categories: opens vs closes
        # opens: "(", "[", "{"
        # closes: ")", "]", "}"
        closes_to_opens = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        # create a stack that holds the opens
        opens_stacks = []

        for c in s:
            if c in ("(", "[", "{"):
                opens_stacks.append(c)
            else:
                if len(opens_stacks) == 0 or opens_stacks.pop() != closes_to_opens[c]:
                    return False

        return True if not opens_stacks else False