"""
Write a program that takes a double x and an integer y and returns x^y
"""

def power(x: float, y: int) -> float:

    result = x
    for i in range(y):
        result *= x
    return result


def test_1():
    