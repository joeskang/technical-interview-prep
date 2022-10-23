"""
can you sum the elements in a given array to match the target? (repeats of elements allowed)

ex: [5, 3, 4, 7]:
* yes, 3 + 4 = 7 or 7 = 7
"""

def canSum(target: int, nums: list) -> bool:
    cache = {} # keys: current number (after subtraction), values: boolean

    # edge cases:
    if 1 in nums:
        return True
    if not nums or min(nums) > target:
        return False

    def can_i_sum(current, subtract):
        if current in cache:
            return cache[current]

        can_not_sum = True

        if subtract > current:
            return can_not_sum

        if subtract == current:
            return False

        current -= subtract

        for num in nums:
            can_not_sum &= can_i_sum(current, num)

        cache[current] = can_not_sum
        return can_not_sum

    return not can_i_sum(target, 0)

if __name__ == "__main__":
    print(canSum(9, [5, 3, 4, 7]))
