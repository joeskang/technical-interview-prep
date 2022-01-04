<<<<<<< Updated upstream
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:

        closest = None
        '''
        for l in range(len(nums) - 2):
            for m in range(l+1, len(nums)-1):
                for r in range(m+1, len(nums)):
                    sum_ = nums[l] + nums[m] + nums[r]
                    if closest is None or abs(sum_ - target) < closest:
                        closest = sum_
                    if closest == 0:
                        break
        '''
        nums.sort()
        for l in range(len(nums)):
            m, r = l + 1, len(nums) - 1
            while m < r:

                sum_ = nums[l] + nums[m] + nums[r]
                if closest is None or abs(target - sum_) < abs(target - closest):
                    closest = sum_
                if sum_ > target:
                    r -= 1
                else:
                    m += 1

                if sum_ == target:
                    break

        return closest

sol = Solution()
print(sol.threeSumClosest([0,2,1,-3], 1))
=======
def noPrefix(words):
    # Write your code here
    myd = {}

    for word in words:
        # check if word exists condition
        if word in myd:
            print("BAD SET")
            print(word)
            return

        substring = ''
        for j in range(len(word)):
            substring += word[j]
            if substring in myd:
                print("BAD SET")
                print(word)
                return

        for w in myd:


        myd[word] = True

    print("GOOD SET")
    return


if __name__ == '__main__':
    words =[
        'hgiiccfchbeadgebc',
        'biiga',
        'edchgb',
        'ccfdbeajaeid',
        'ijgbeecjbj',
        'bcfbbacfbfcfbhcbfjafibfhffac',
        'ebechbfhfcijcjbcehbgbdgbh',
        'ijbfifdbfifaidje',
        'acgffegiihcddcdfjhhgadfjb',
        'ggbdfdhaffhghbdh',
        'dcjaichjejgheiaie',
        'd',
        'jeedfch',
        'ahabicdffbedcbdeceed',
        'fehgdfhdiffhegafaaaiijceijdgbb',
        'dbeedfdjaghbhgdhcedcj',
        "decjacchhaciafafdgha",
    ]
    noPrefix(words)
>>>>>>> Stashed changes
