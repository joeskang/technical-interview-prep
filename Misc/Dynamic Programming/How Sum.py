"""
how can you sum the elements in a given array to match the target? (repeats of elements allowed)

ex: [5, 3, 4, 7]:
* yes, 3 + 4 = 7 or 7 = 7
"""


def main(t, nums):
    cache = {} # keys: current, values: list

    def howSum(target: int, numbers,):

        if target in cache:
            return cache[target]

        if target == 0:
            return []
        if target < 0:
            return None

        for num in numbers:
            remainder = target - num
            remainder_result = howSum(remainder, numbers)

            if remainder_result is not None:

                cache[target] = remainder_result + [num]
                return cache[target]

        return None

    return howSum(t, nums)


if __name__ == "__main__":
    print(main(1000, [7, 3, 5]))