from typing import List
import math
from itertools import repeat


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        min_num_changes = list(repeat(math.inf, amount + 1))
        min_num_changes[0] = 0
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    num_changes = min_num_changes[i - coins[j]] + 1
                    if num_changes < min_num_changes[i]:
                        min_num_changes[i] = num_changes

        if min_num_changes[amount] == math.inf:
            return -1
        return min_num_changes[amount]
