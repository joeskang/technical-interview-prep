class Solution:
    def myAtoi(self, s: str) -> int:

        # eliminate whitespace
        s = s.strip()

        num = 0
        negative = False
        first_nonzero = False
        # won't know the length of the number until actually read, so utilize stack style
        digits = []
        for i in range(len(s)):
            char = s[i]

            if char == '-' and i == 0:
                negative = True

            elif char == '0' and not first_nonzero:
                continue

            elif char.isnumeric():
                # num += int(char) * 10**(len(s) - 1 - i)
                digits.append(int(char))
                if not first_nonzero:
                    first_nonzero = True

            elif char == "+" and i == 0:
                negative = False

            else:
                break

        index = 0
        while digits:
            num += digits.pop() * 10**index
            index += 1

        if negative:
            num *= -1
            if num < -2**31:
                num = -2**31
        elif num > 2**31 - 1:
            num = 2**31 - 1

        return num

if __name__ == "__main__":
    sol = Solution()
    # ans = sol.myAtoi("42")
    # assert ans == 42
    #
    # ans = sol.myAtoi("        -42")
    # assert ans == -42
    #
    # ans = sol.myAtoi(" -42 with words")
    # print(ans)
    ans = sol.myAtoi("21474836460")
