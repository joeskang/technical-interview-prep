"""
date: June 26, 2022
total time: 00:12:34
"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counts = {}
        # keys = word (lowercase)
        # vals = counts

        punctuations = [
            "!", "?", "'", ",", ";", "."
        ]

        # omit punctuations
        for p in punctuations:
            paragraph = paragraph.replace(p, '') if p not in (",") else paragraph.replace(p, " ")

        words = paragraph.split(' ')

        for word in words:
            word = word.lower()
            if word in banned or word == "":
                continue
            counts[word] = 1 if word not in counts else counts[word] + 1
            # print(counts)

        max_count, common_word = 0, None
        for k, v in counts.items():
            if v > max_count:
                max_count = v
                common_word = k

        return common_word