from typing import List
import heapq


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # Worst case nlog(n) solution with O(n) space
        if len(nums) == 1:
            return nums[0]
        # Initialize a list of best results to the length of nums array
        min_heap = [(-nums[0], 0)]
        for idx in range(1, len(nums)):
            while min_heap[0][1] < idx - k:
                heapq.heappop(min_heap)
            if idx == len(nums) - 1:
                return -min_heap[0][0] + nums[idx]
            heapq.heappush(min_heap, (min_heap[0][0] - nums[idx], idx))


if __name__ == "__main__":
    nums_1 = [1, -1, -2, 4, -7, 3]
    k_1 = 2
    nums_2 = [10, -5, -2, 4, 0, 3]
    k_2 = 3
    nums_3 = [1, -5, -20, 4, -1, 3, -6, -3]
    k_3 = 2
    sol = Solution()
    assert sol.maxResult(nums_1, k_1) == 7
    assert sol.maxResult(nums_2, k_2) == 17
    assert sol.maxResult(nums_3, k_3) == 0
    print("All good!")
