from typing import List


class Solution:
    digit_to_letter = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def __init__(self):
        self.results = []
        self.digits = ""

    def letterCombinations(self, digits: str) -> List[str]:
        self.digits = digits
        self._backtrack(cur_str=[], cur_idx=0)
        return self.results

    def _backtrack(self, cur_str: list[str], cur_idx: int):
        if len(cur_str) == len(self.digits):
            self.results.append("".join(cur_str))

        for i, digit in enumerate(self.digits[cur_idx:]):
            letters = self.digit_to_letter[digit]
            next_idx = cur_idx + i + 1
            for letter in letters:
                cur_str.append(letter)
                self._backtrack(cur_str, next_idx)
                cur_str.pop()
