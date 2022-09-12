class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {k: v for v, k in enumerate(nums)}
        for idx, num in enumerate(nums):
            conjugate = target - num
            if conjugate in nums_map:
                conjugate_idx = nums_map[conjugate]
                if conjugate_idx != idx:
                    return [idx, conjugate_idx]
