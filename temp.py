

"""jump up stairs problem"""

def solution(num):
    # need to iterate through integers less than num

    return 2**(num - 1)



def recur_count(count, num, div):
    if num < div:
        return 0
    else:

        return recur_count(count, num, div)
