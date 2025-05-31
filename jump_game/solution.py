from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        num_elements = len(nums)
        if num_elements == 1:
            return True
        furthest_idx = 0
        for idx, num in enumerate(nums):
            curr_furthest_possible = idx + num
            if curr_furthest_possible > furthest_idx:
                furthest_idx = curr_furthest_possible
            if curr_furthest_possible >= num_elements - 1:
                return True
            if furthest_idx == idx:
                return False
        