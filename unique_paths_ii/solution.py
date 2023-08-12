from typing import List


class Solution:
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.obstacle_grid = obstacleGrid
        self.num_rows = len(obstacleGrid)
        self.num_cols = len(obstacleGrid[0])
        self.is_visited = [[False for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        self.num_paths = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        self.num_paths[self.num_rows - 1][self.num_cols - 1] = 1
        return self.dfs(0, 0)
    
    def dfs(self, cur_row: int, cur_col: int) -> int:
        if cur_row == self.num_rows or cur_col == self.num_cols or self.obstacle_grid[cur_row][cur_col] == 1:
            return 0
        elif self.is_visited[cur_row][cur_col]:
            return self.num_paths[cur_row][cur_col]
        
        self.is_visited[cur_row][cur_col] = True
        if cur_row == self.num_rows - 1 and cur_col == self.num_cols - 1:
            return self.num_paths[cur_row][cur_col]
        num_paths = self.dfs(cur_row + 1, cur_col)
        num_paths += self.dfs(cur_row, cur_col + 1)
        self.num_paths[cur_row][cur_col] = num_paths
        return num_paths
        
        