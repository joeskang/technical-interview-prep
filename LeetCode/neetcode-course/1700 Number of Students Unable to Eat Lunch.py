"""

incomplete
"""

def solution(students: list, sandwiches: list) -> int:
    fed_students = 0

    while students:
        past_length = len(students)
        new_queue = []
        for i, student in enumerate(students):
            if student != sandwiches[0]:
                new_queue.append(student)
            else:
                students = students[:i] + students[i+1:]
                sandwiches = sandwiches[1:]
                if not sandwiches:
                    return fed_students
                fed_students += 1
        if len(new_queue) == past_length:
            return fed_students
    return fed_students

