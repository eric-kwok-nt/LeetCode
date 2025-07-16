from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        new_board = [[0 for _ in board[0]] for _ in board]
        for row_idx, row in enumerate(board):
            for col_idx, col_element in enumerate(row):
                num_neighbours = self.get_num_neighbours(board, row_idx, col_idx)
                if num_neighbours > 3:
                    new_board[row_idx][col_idx] = 0
                elif num_neighbours == 2:
                    new_board[row_idx][col_idx] = col_element
                elif num_neighbours == 3:
                    new_board[row_idx][col_idx] = 1

        for row_idx, row in enumerate(new_board):
            board[row_idx] = row

    def get_num_neighbours(
        self, board: List[List[int]], row_idx: int, col_idx: int
    ) -> int:
        num_neighbours = 0
        for r in range(max(0, row_idx - 1), min(len(board), row_idx + 2)):
            for c in range(max(0, col_idx - 1), min(len(board[0]), col_idx + 2)):
                if r == row_idx and c == col_idx:
                    continue
                num_neighbours += board[r][c]
        return num_neighbours
