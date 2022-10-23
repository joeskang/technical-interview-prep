"""
Datetime: June 26, 2022, 10:59 PM
Total time: 00:34:50 (I left the stopwatch running and forgot about it when making coffee)
"""


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_log_dict = {}  # keys: content of log, vals: [indices]
        num_logs = []  # maintains order (FIFO queue)

        # digitals = [f"{i}" for i in range(10)]

        for log in logs:
            identifier = log.split(" ")[0]

            if log.split(" ")[1].isnumeric():
                num_logs.append(log)
            elif len(log.split(" ")) == 0:
                continue
            else:
                substring = log[log.index(" ") + 1:]
                letter_log_dict[substring] = [identifier] if substring not in letter_log_dict else letter_log_dict[
                                                                                                       substring] + [
                                                                                                       identifier]
                print(letter_log_dict)

        substrings = list(letter_log_dict.keys())
        substrings.sort()

        response = []
        for s in substrings:
            identifiers = letter_log_dict[s]
            if len(identifiers := letter_log_dict[s]) > 1:
                identifiers.sort()
                for identifier in identifiers:
                    response.append(" ".join([identifier, s]))
            else:
                response.append(" ".join([identifiers[0], s]))

        for num_log in num_logs:
            response.append(num_log)

        return response