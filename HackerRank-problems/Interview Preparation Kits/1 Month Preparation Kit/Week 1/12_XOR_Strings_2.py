"""
!! This is one of the buggiest problems that I've seen on HackerRank
the answer was partially written, but you can't find the answer any other way
* I tried using ternary operators to return the same answer and it was marked incorrect

Time: 00:06:51 (most of this time was spent figuring out how to work around the bug)
Date = June 08, 2022
"""
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0';
        else:
            res += '1';

    return res

s = input()
t = input()
print(strings_xor(s, t))
