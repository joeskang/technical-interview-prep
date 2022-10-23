class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_count = 0

        curr_max = 0
        if len(fruits) <= 2:
            return len(fruits)

        type_1 = fruits[0]
        type_2 = fruits[1]

        two_count = 0
        cur_count = 0
        for i in range(2, len(fruits)):
            cur_fruit = fruits[i]

            if cur_fruit == type_2:
                two_count += 1
            elif cur_fruit == type_1:
                cur_count += two_count
                two_count = 1
            else:
                type_1 = type_2, type_2 = cur_fruit
                two_count = 1

       # TODO: continue from here