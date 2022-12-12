"""
not my solution, but impressed by elegant solution
"""

from collections import Counter

class Solution:

    def countStudents(self, students: list, sandwiches: list) -> int:
        count_ = Counter(students)

        for sandwich in sandwiches:
            if count_[sandwich] == 0:
                break
            count_[sandwich] -= 1
        return count_[0] + count_[1]