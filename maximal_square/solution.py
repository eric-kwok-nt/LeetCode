from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * (cols + 1)
        max_side = 0
        prev = 0  # top-left from previous row

        for i in range(1, rows + 1):
            prev = 0
            for j in range(1, cols + 1):
                temp = dp[j]
                if int(matrix[i - 1][j - 1]):
                    dp[j] = 1 + min(dp[j], dp[j - 1], prev)
                    max_side = max(max_side, dp[j])
                else:
                    dp[j] = 0
                prev = temp

        return max_side * max_side


if __name__ == "__main__":
    sol = Solution()

    # matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    # matrix = [["0","1"],["1","0"]]
    # matrix = [["0","1"]]
    matrix = [
        ["0", "0", "0", "1"],
        ["1", "1", "0", "1"],
        ["1", "1", "1", "1"],
        ["0", "1", "1", "1"],
        ["0", "1", "1", "1"],
    ]
    print(sol.maximalSquare(matrix))
