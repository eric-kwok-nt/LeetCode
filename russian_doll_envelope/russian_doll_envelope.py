from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # sort width of envelope in increasing order while the height in decreasing order
        envelopes = sorted(envelopes, key=lambda x: [x[0], -x[1]])

        height_list = []
        for _, height in envelopes:
            target_idx = self.find_next_largest_height(height_list, height)
            if target_idx == len(height_list):
                height_list.append(height)
            else:
                # Target index always point to height element >= current height
                # Aims to record the best combination of envelope heights
                height_list[target_idx] = height

        return len(height_list)

    def find_next_largest_height(
        self, height_list: List[int], target_height: int
    ) -> int:
        left, right = 0, len(height_list) - 1
        while right >= left:
            # Right bit shift == divide by 2 and floor
            mid = (left + right) >> 1
            if height_list[mid] >= target_height:
                right = mid - 1
            else:
                left = mid + 1

        # left always ends up being 1 bigger than right
        return left


if __name__ == "__main__":
    Sol = Solution()
    input_list = [[5, 4], [6, 4], [6, 7], [2, 3]]
    print(Sol.maxEnvelopes(input_list))
