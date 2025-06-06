from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset_list = [[]]
        self.create_subset(nums, [], -1, subset_list)
        return subset_list

    def create_subset(
        self,
        nums: List[int],
        curr_subset: List[int],
        idx: int,
        subset_list: List[List[int]],
    ):
        for i in range(idx + 1, len(nums)):
            new_subset = curr_subset.copy()
            new_subset.append(nums[i])
            subset_list.append(new_subset)
            self.create_subset(nums, new_subset, i, subset_list)


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        num_elements = len(nums)
        total_num_combi = 2**num_elements - 1
        subset_list = [[]]
        for i in range(1, total_num_combi+1):
            subset = []
            for j in range(num_elements):
                if i & 1:
                    subset.append(nums[j])
                i = i >> 1
            subset_list.append(subset)
            
        return subset_list