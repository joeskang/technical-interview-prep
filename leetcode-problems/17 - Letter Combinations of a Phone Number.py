class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        myd = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        output = []
        for d in digits:

            chars = list(myd[d])
            if len(output) == 0:
                output = chars
                continue
            newl = []
            for c in chars:
                copy_ = list(output)
                while copy_:
                    subs = copy_.pop()
                    newl.append(subs + c)
            output = newl

        return output