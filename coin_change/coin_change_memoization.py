from typing import List
import math


class Solution:
    def __init__(self):
        self.changes = dict()

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        number_of_coins = self._coinChanger(amount)
        if number_of_coins == math.inf:
            return -1
        return number_of_coins

    def _coinChanger(self, remainder: int):
        if remainder < 0:
            return math.inf
        elif remainder == 0:
            return 0
        elif remainder in self.changes:
            return self.changes[remainder]

        self.changes[remainder] = min(
            self._coinChanger(remainder - coin) + 1 for coin in self.coins
        )
        return self.changes[remainder]
