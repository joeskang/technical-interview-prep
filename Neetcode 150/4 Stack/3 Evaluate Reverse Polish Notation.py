def evalRPN(tokens) -> int:
    my_stack = []

    for num in tokens:

        match num:
            case '+':
                my_stack.append(my_stack.pop() + my_stack.pop())

            case '-':
                a, b = my_stack.pop(), my_stack.pop()
                my_stack.append(b - a)

            case '*':
                my_stack.append(my_stack.pop() * my_stack.pop())

            case '/':
                a, b = my_stack.pop(), my_stack.pop()
                my_stack.append(int(b/a))

            case other:
                my_stack.append(int(num))

    return my_stack.pop() if my_stack else 0


def test1():
    tokens = ['2', '1', '+', '3', '*']

    assert evalRPN(tokens) == 9


def main():
    test1()

if __name__ == '__main__':
    main()