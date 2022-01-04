class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary = format(n, 'b')[::-1]

        output = 0
        for i in range(len(binary)):
            c = binary[i]
            if c == '0':
                output += 2 ** i

        return output