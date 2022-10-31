

"""
sort list with even numbers in the beginning


"""

def sortArray(nums: list) -> list:
    current = odd = unclassified = 0
    while unclassified < len(nums):
        unclassified += 1
        if nums[current] % 2 == 0:
            current 