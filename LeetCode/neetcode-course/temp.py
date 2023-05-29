def subarraySum(arr):
    # Write your code here

    result = 0
    # 1 ... len(arr)
    for i in range(1, len(arr) + 1):
        # initialize
        l, r = 0, i

        while r < len(arr):
            subarray = arr[l:r]
            result += sum(arr[l:r])

            r += 1
            l += 1

    return result

if __name__ == '__main__':
    subarraySum([1,2,3])