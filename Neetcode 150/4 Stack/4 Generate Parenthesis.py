"""
innovative approach using 1 defined stack + 1 defined list + stack trace
credit to neetcode
--> 2 stacks + 1 array
"""
def generateParenthesis(n: int) -> list:
    temp_stack = []
    result_stack = []

    def inner_function(left_iter, right_iter):
        print(f"left and right: {left_iter} {right_iter}")

        # base case of left_iter == right_iter
        if left_iter == right_iter == n:
            result_stack.append(''.join(temp_stack))
            """
                as we return from here, we go back in the stack trace to the numerous
                inner_function() calls. initially, this will reset the right_iter to 0
                on the first return
            """
            return

        if left_iter < n:
            temp_stack.append('(')
            inner_function(left_iter + 1, right_iter)
            temp_stack.pop()

        if right_iter < left_iter:
            temp_stack.append(')')
            inner_function(left_iter, right_iter + 1)
            temp_stack.pop()

    inner_function(0, 0)
    return result_stack

def test1():
    '''
        in order of the calls to the inner function, left and right will be the following values:

        left and right: 0 0 -->
        left and right: 1 0 --> (
        left and right: 2 0 --> ((
        left and right: 3 0 --> (((
        left and right: 3 1 --> ((()
        left and right: 3 2 --> ((())
        left and right: 3 3 --> appends ((()))
        left and right: 2 1 --> (()
        left and right: 3 1 --> (()(
        left and right: 3 2 --> (()()
        left and right: 3 3 --> appends (()())
        left and right: 2 2 --> (())
        left and right: 3 2 --> (())(
        left and right: 3 3 --> appends (())()
        left and right: 1 1 --> ()
        left and right: 2 1 --> ()(
        left and right: 3 1 --> ()((
        left and right: 3 2 --> ()(()
        left and right: 3 3 --> appends ()(())
        left and right: 2 2 --> ()()
        left and right: 3 2 --> ()()(
        left and right: 3 3 --> appends ()()()
    '''
    result = generateParenthesis(3)
    print(result)
    assert result == ["((()))","(()())","(())()","()(())","()()()"]

if __name__ == "__main__":
    test1()