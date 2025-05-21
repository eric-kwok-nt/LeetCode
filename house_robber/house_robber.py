from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        else:
            prev2, prev1 = nums[0], max(nums[:2])
            for idx, num in enumerate(nums[2:]):
                current = max(prev1, prev2 + num)
                prev2, prev1 = prev1, current
        return current