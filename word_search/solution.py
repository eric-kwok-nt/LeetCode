from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row_idx, row in enumerate(board):
            for col_idx, char in enumerate(row):
                if char == word[0]:
                    checked_pos_set = {(row_idx, col_idx)}
                    exists = self.check_neighbours(
                        board,
                        word,
                        row_idx,
                        col_idx,
                        checked_pos_set=checked_pos_set,
                        word_idx=0,
                    )
                    if exists:
                        return True
        return False

    def check_neighbours(
        self,
        board: List[List[str]],
        word: str,
        row_idx: int,
        col_idx: int,
        checked_pos_set: set[tuple[int, int]],
        word_idx: int,
    ) -> bool:
        if word_idx == len(word):
            return True
        if board[row_idx][col_idx] != word[word_idx]:
            return False
        elif word_idx == len(word) - 1:
            return True
        else:
            exists = False
            checked_pos_set.add((row_idx, col_idx))
            if row_idx + 1 < len(board) and self.check_if_not_prev_square(
                row_idx + 1, col_idx, checked_pos_set
            ):
                exists |= self.check_neighbours(
                    board,
                    word,
                    row_idx + 1,
                    col_idx,
                    checked_pos_set.copy(),
                    word_idx + 1,
                )
            if col_idx + 1 < len(board[0]) and self.check_if_not_prev_square(
                row_idx, col_idx + 1, checked_pos_set
            ):
                exists |= self.check_neighbours(
                    board,
                    word,
                    row_idx,
                    col_idx + 1,
                    checked_pos_set.copy(),
                    word_idx + 1,
                )
            if row_idx - 1 >= 0 and self.check_if_not_prev_square(
                row_idx - 1, col_idx, checked_pos_set
            ):
                exists |= self.check_neighbours(
                    board,
                    word,
                    row_idx - 1,
                    col_idx,
                    checked_pos_set.copy(),
                    word_idx + 1,
                )
            if col_idx - 1 >= 0 and self.check_if_not_prev_square(
                row_idx, col_idx - 1, checked_pos_set
            ):
                exists |= self.check_neighbours(
                    board,
                    word,
                    row_idx,
                    col_idx - 1,
                    checked_pos_set.copy(),
                    word_idx + 1,
                )
            return exists

    def check_if_not_prev_square(
        self, next_row_idx, next_col_idx, checked_pos_set
    ) -> bool:
        return (next_row_idx, next_col_idx) not in checked_pos_set


if __name__ == "__main__":
    board = [["a", "b"]]
    word = "ba"
    sol = Solution()
    print(sol.exist(board, word))
