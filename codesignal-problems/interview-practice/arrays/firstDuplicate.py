# firstDuplicate.txt

def solution(a):
    occurrences = {}
    for i in range(len(a)):
        num = a[i]
        if num in occurrences:
            return num
        occurrences[num] = True

    return -1