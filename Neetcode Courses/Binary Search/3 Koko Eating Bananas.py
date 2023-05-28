"""
https://leetcode.com/problems/koko-eating-bananas/

875. Koko Eating Bananas
"""


def minEatingSpeed(piles: list, h: int) -> int:
    import math

    # binary search where left = 1, right = max(piles0)
    left, right = 1, max(piles)

    find_hours = lambda choice: sum([math.ceil(pile / choice) for pile in piles])

    min_choice = right

    while left <= right:
        mid = left + (right - left) // 2
        if (result := find_hours(mid)) < h:
            min_choice = min(min_choice, result)
            right = mid - 1

        elif result == h:
            return mid
        else:
            left = mid + 1

    return min_choice


def test1():
    my_arr = [3, 6, 7, 11]
    assert minEatingSpeed(my_arr, 8) == 4


if __name__ == "__main__":
    test1()
