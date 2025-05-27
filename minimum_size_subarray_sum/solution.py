from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        total_num_ele = len(nums)
        min_length = total_num_ele
        left_ptr = 0
        right_ptr = 1
        curr_sum = nums[0]
        while True:
            if curr_sum >= target:
                curr_min_length = right_ptr - left_ptr
                if curr_min_length < min_length:
                    min_length = curr_min_length
                curr_sum -= nums[left_ptr]
                left_ptr += 1
                if left_ptr == right_ptr:
                    return min_length
            elif right_ptr < total_num_ele:
                curr_sum += nums[right_ptr]
                right_ptr += 1
            else:
                return min_length
