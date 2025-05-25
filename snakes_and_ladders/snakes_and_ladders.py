from typing import List
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board = self.rearrange_board(board)
        total_num_sq = len(board)
        if total_num_sq == 2:
            return 1
        costs = [0]
        costs.extend([float("inf")] * (total_num_sq - 1))
        next_steps = deque([0])
        while len(next_steps) != 0:
            curr_step = next_steps.popleft()
            for i in range(1, 7):
                next_step = curr_step + i
                if next_step >= total_num_sq:
                    continue
                if board[next_step] != -1:
                    next_step = board[next_step] - 1
                if next_step == total_num_sq - 1:
                    return costs[curr_step] + 1
                if costs[next_step] == float("inf"):
                    costs[next_step] = costs[curr_step] + 1
                    next_steps.append(next_step)
        return -1
        
    def rearrange_board(self, board: List[List[int]]) -> List[int]:
        board = board[::-1]
        n = len(board)
        arr = []
        for i in range(n):
            if i & 1:
                # odd row
                arr.extend((board[i][::-1]))
            else:
                arr.extend(board[i])
        return arr


board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
# board = [[-1,-1,-1],[-1,9,8],[-1,8,9]]
# board = [[-1,-1,30,14,15,-1],[23,9,-1,-1,-1,9],[12,5,7,24,-1,30],[10,-1,-1,-1,25,17],[32,-1,28,-1,-1,32],[-1,-1,23,-1,13,19]]

sol = Solution()
print(sol.snakesAndLadders(board))