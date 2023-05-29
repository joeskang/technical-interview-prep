class Solution:
    def evalRPN(self, tokens: list) -> int:

        operations = {'+', '-', '/', '*'}
        temp_stack = [] # should only contain left and right inputs

        for token in tokens:
            if token in operations:
                second = temp_stack.pop()
                first = temp_stack.pop()
                assert len(temp_stack) == 0

                if token == '+':
                    temp_stack.append(first + second)
                elif token == '-':
                    temp_stack.append(first - second)
                elif token == '*':
                    temp_stack.append(first * second)
                else:
                    temp_stack.append()




def test_solution():
    sol = Solution()
    l1 = ['2', '1', '+', '3', '*']
    assert sol.evalRPN(l1) == 9

if __name__ == "__main__":
    test_solution()