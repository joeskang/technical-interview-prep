
"""
swap the ith and jth bits of a number

"""

def main(number, i, j):

    # check to see if the ith and jth bits are different
    # if they're the same, no need to do anything
    if (number >> i) & 1 != (number >> j) & 1:
        # move a 1 to the ith spot and jth spot
        # use bitwise OR to combine them
        bit_mask = (1 << i) | (1 << j)

        # then, apply bit_mask to the number
        # an XOR will efficiently swap out the 0s to 1s and vice versa
        number ^= bit_mask
    return number

if __name__ == "__main__":
    print(main(22, 3,4))