"""
Runtime: 70 ms, faster than 5.06% of Python3 online submissions for Text Justification.
Memory Usage: 14.3 MB, less than 79.40% of Python3 online submissions for Text Justification.
"""
class Solution:
    def fullJustify(self, words, maxWidth: int):

        current_line = []
        current_length = 0
        output = []

        def make_string(l, last=False):
            out = ''
            if len(l) == 1 or last:
                for i in range(len(l)):
                    if i < len(l) - 1:
                        out += l[i] + ' '
                    else:
                        out += l[i]
                for i in range(maxWidth - len(out)):
                    out += ' '
                return out
            chars_only = 0
            for w in l:
                chars_only += len(w)
            remainder = maxWidth - chars_only
            extra = remainder % (len(l) - 1)

            for i in range(len(l)):
                if i < len(l) - 1:
                    out += l[i] + ''.join(' ' for _ in range(remainder // (len(l) - 1)))
                    if extra:
                        out += ' '
                        extra -= 1
                else:
                    out += l[i]
            return out


        last_line = False
        for i in range(len(words)):
            word = words[i]
            if i == len(words) - 1:
                last_line = True
            if len(current_line) == 0 and len(word) == maxWidth:
                output.append(make_string([word]))
                continue

            if len(word) + current_length + 1 > maxWidth:
                output.append(make_string(current_line))
                current_line = [word]
                current_length = len(word)
            else:
                current_line.append(word)
                if current_length == 0:
                    current_length = len(word)
                else:
                    current_length += len(word) + 1

        if current_line:
            output.append(make_string(current_line, True))

        return output


sol = Solution()
# myl = ["What", "must", "be", "acknowledgment", "shall", "be"]
myl = ['a','b','c','d','e']

max_width =3

x = sol.fullJustify(myl, max_width)
print(x)