

class Solution:
    def twoSum(self, nums, target: int):

        val_dict = {}

        # find the difference of target and each val
        for i in range(len(nums)):
            other = target - nums[i]

            if other in val_dict:
                return [i, val_dict[other]] if i < val_dict[other] else [val_dict[other], i]

            val_dict[nums[i]] = i


        return []

if __name__ == "__main__":
    sol = Solution()
    # ans = sol.twoSum([2, 7, 11, 15], 9)

    # assert ans == [0,1]

    # ans = sol.twoSum([3,2,4], 6)
    # assert ans == [1,2]

    ans = sol.twoSum([3,3], 6)
    assert ans == [0,1
                   ]