"""

How would you compute the parity of a very large number of 64-bit words?

"""

def parity(num: int) -> int:

    result = 0
    while num:
        result ^= num & result
        num >>= 1

    return result

def test_1():
    assert parity(12) == 0

def test_2():
    assert parity(1234) == 1

if __name__ == '__main__':
    test_1()
    test_2()
