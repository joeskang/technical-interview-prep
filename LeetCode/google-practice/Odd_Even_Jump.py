
class List(list):
    def __init__(self):
        super()

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:

        def higher(start_index):
            # will have to naive lowest higher search
            lowest_high = None
            target_index = None
            mynum = arr[start_index]
            for i in range(start_index + 1, len(arr)):
                num = arr[i]
                if num > mynum and (lowest_high is not None and num < lowest_high):
                    lowest_high = num
                    target_index = i

            return target_index, lowest_high
            
        def lower(start_index):

            highest_low = None
            target_index = None
            mynum = arr[start_index]

            for i in range(start_index + 1, len(arr)):
                num = arr[i]
                if num < mynum and (highest_low is not None and num > highest_low):
                    highest_low = num
                    target_index = i

            return target_index, highest_low

        myd = {}

        def recursion(index):
            if index == len(arr) - 1:
                
            