class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        group_names = {
            1: '',
            2: ' Thousand',
            3: ' Million',
            4: ' Billion'
        }

        digit_names = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
            19: "Nineteen", 20: "Twen", 30: "Thir", 40: "For", 50: "Fif",
            60: "Six", 70: "Seven", 80: "Eigh", 90: "Nine", 0: ''
        }

        digits = []
        current_group = []
        while num:
            current_group.append(num % 10)
            num //= 10
            if len(current_group) == 3 or num == 0:
                digits.append(current_group)
                current_group = []

        return_string = group_string = ''
        while digits:
            group_choice = len(digits)

            current_group = digits.pop()
            has_nonzero = False
            while current_group:
                place_value = len(current_group)
                curr_digit = current_group.pop()

                if curr_digit == 0:
                    if place_value == 1 and has_nonzero:
                        group_string += group_names[group_choice]
                    continue

                has_nonzero = True

                if place_value == 3:
                    group_string += f" {digit_names[curr_digit]} Hundred"

                elif place_value == 2:

                    if curr_digit != 1:
                        group_string += f" {digit_names[curr_digit * 10]}ty"
                    elif curr_digit == 1:
                        units_place = current_group.pop()
                        curr_digit = curr_digit * 10 + units_place
                        group_string += f" {digit_names[curr_digit] + group_names[group_choice]}"
                else:
                    group_string += f" {digit_names[curr_digit] + group_names[group_choice]}"

        return group_string[1:]