from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if all(num < 0 for num in nums):
            return max(nums)
        curr_sum = 0
        max_sum = 0
        for num in nums:
            if num > 0 and curr_sum < 0:
                curr_sum = num
            else:
                curr_sum += num
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum


if __name__ == "__main__":
    sol = Solution()

    input_arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(sol.maxSubArray(input_arr))
