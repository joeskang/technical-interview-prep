class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # quick and easy naive approach
        # edge case: zeros in list

        single_zero_index = None

        # handle zeros
        if (zero_count := nums.count(0)) > 0:
            if zero_count > 1:
                for _ in range(len(nums)):
                    nums[_] = 0
                return

            single_zero_index = nums.index(0)

        # find total product
        total_product = 1
        for i in range(len(nums)):
            if i != single_zero_index:
                n = nums[i]
                total_product *= n

        for i in range(len(nums)):
            if single_zero_index is not None:
                nums[i] = total_product if i == single_zero_index else 0
            else:
                nums[i] = int(total_product / nums[i])
        return nums