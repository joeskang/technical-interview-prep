"""

"""
import unittest

# determine parity of numbers
# parity: 1 if count(1s) is odd, else 0

def brute_force(number):
    """
        XOR needed to switch on/off the response
        O(n) solution
    :param number:
    :return:
    """
    # bit_count = 0
    response = 0
    while number:
        # bit_count += number & 1
        response ^= number & 1
        number >>= 1
    # return 1 if bit_count % 2 else 0
    return response

def first_improvement(number):
    """
        @@@@@ Remember @@@@@:
        x & (x - 1) erases the lowest set bit

    :param number:
    :return:
    """
    response = 0
    while number:
        response ^= 1 # flip flop between on and off
        number &= number - 1

    return response


def run_tests(functions):
    for function in functions:
        assert function(11) == 1, "Should be 1"
        assert function(10) == 0, "Should be 0"


def main():
    functions = [brute_force, first_improvement]
    run_tests(functions)


if __name__ == "__main__":
    main()
