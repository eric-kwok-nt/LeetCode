from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        record = 0
        for num in nums:
            tmp = record | (1 << num)
            if record == tmp:
                return num
            else:
                record = tmp


if __name__ == "__main__":
    Sol = Solution()
    # nums = [1, 3, 4, 2, 2]
    nums = [3, 1, 3, 4, 2]
    print(Sol.findDuplicate(nums))
