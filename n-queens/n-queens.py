from typing import List, Set


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.result: List[List[int]] = []
        self.dfs([], set(), set(), set())

        return [
            ["." * col + "Q" + "." * (self.n - col - 1) for col in solution]
            for solution in self.result
        ]

    def dfs(
        self,
        queens: List[int],
        queens_set: Set[int],
        xy_diff: Set[int],
        xy_sum: Set[int],
    ):
        """Whenever a location (x, y) is occupied, any other
        locations (p, q) where p + q == x + y, or p - q == x - y
        would be invalid.

        Args:
            queens (List[int]): queens[0] == 1 means queen is
            queens_set (Set[int]): set of all queens
            located at row 0 col 1
            xy_diff (Set[int]): Set of all (x - y)
            xy_sum (Set[int]): Set of all (x + y)
        """
        p = len(queens)
        if p == self.n:
            self.result.append(queens)
            return
        for q in range(self.n):
            if q not in queens_set and p - q not in xy_diff and p + q not in xy_sum:
                self.dfs(
                    queens + [q], queens_set | {q}, xy_diff | {p - q}, xy_sum | {p + q}
                )


if __name__ == "__main__":
    n = 4
    Sol = Solution()
    print(Sol.solveNQueens(n))
