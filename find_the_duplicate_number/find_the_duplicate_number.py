from typing import List


class Solution:
    """Referenced from https://www.youtube.com/watch?v=wjYnzkAhcNk"""

    def findDuplicate(self, nums: List[int]) -> int:
        slow_pointer = 0
        fast_pointer = 0

        while True:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[nums[fast_pointer]]

            if slow_pointer == fast_pointer:
                break

        fast_pointer = 0

        while True:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[fast_pointer]

            if slow_pointer == fast_pointer:
                return slow_pointer


if __name__ == "__main__":
    Sol = Solution()
    # nums = [1, 3, 4, 2, 2]
    nums = [3, 1, 3, 4, 2]
    print(Sol.findDuplicate(nums))
