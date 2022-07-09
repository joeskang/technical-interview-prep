import math


def counterGame(n):
    # Write your code here

    # edge case:
    if n == 1:
        return "Louise"

    louise_won = False

    # let's use logarithms
    while n > 1:
        # if we need to append powers of two
        if not math.log(n, 2).is_integer():
            temp = int(math.log(n, 2))
            n = n - 2 ** temp
        else:
            n //= 2

        louise_won = not louise_won

    return "Louise" if louise_won else "Richard"
