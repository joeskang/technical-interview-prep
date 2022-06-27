"""
Date started: June 26, 2022
time spent this day: 00:16:18

Status: unfinished
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        total_area = local_max = left_pointer = right_pointer = left_height = right_height = 0

        while left_pointer < len(height):
            left_height = height[left_pointer]

            # start of a ditch
            if left_height > local_max:
                local_max = left_height
                potential_area = 0

                while right_pointer < len(height) and right_height < local_max:
                    right_pointer += 1
                    if right_pointer >= len(height):
                        # right_height = height[right_pointer]
                        potential_area = 0
                        break
                    right_height = height[right_pointer]

                    potential_area += (local_max - right_height)

                total_area += potential_area
                left_pointer, left_height, local_max = right_pointer, right_height, 0

            # set right pointer to left pointer
            left_pointer = right_pointer
