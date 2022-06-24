from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longest_seq = 1
        self.nums = set(nums)
        while True:
            try:
                num = self.nums.pop()
                conseq_len = self.check_next(num)
                if conseq_len > longest_seq:
                    longest_seq = conseq_len
            except KeyError:
                return longest_seq

    def check_next(self, num: int, conseq_len: int = 1) -> int:
        if num + 1 in self.nums:
            self.nums.remove(num + 1)
            conseq_len += 1
            conseq_len = self.check_next(num + 1, conseq_len)
        if num - 1 in self.nums:
            self.nums.remove(num - 1)
            conseq_len += 1
            conseq_len = self.check_next(num - 1, conseq_len)
        return conseq_len


if __name__ == "__main__":
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    Sol = Solution()
    print(Sol.longestConsecutive(nums))
