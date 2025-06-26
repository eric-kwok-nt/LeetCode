from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        total_row = len(triangle)
        previous_row_cost = [triangle[0][0]]
        for row in range(1, total_row):
            current_row_cost = []
            for col in range(len(triangle[row])):
                current_row_cost.append(
                    min(
                        previous_row_cost[min(len(previous_row_cost) - 1, col)],
                        previous_row_cost[max(0, col - 1)],
                    )
                    + triangle[row][col]
                )
            previous_row_cost = current_row_cost.copy()
        return min(previous_row_cost)


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

sol = Solution()
print(sol.minimumTotal(triangle=triangle))
