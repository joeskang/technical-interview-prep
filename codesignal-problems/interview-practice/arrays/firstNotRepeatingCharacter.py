def solution(s):
    occur = {}
    for i in range(len(s)):
        char = s[i]
        if char in occur:
            occur[char] += 1
        else:
            occur[char] = 1

    for k, v in occur.items():
        if v == 1:
            return k

    return '_'