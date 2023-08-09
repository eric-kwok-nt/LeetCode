from typing import List
from itertools import repeat
from collections import defaultdict


class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = None
        self.num_reorders = 0

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.visited = list(repeat(False, n))
        self.visited[0] = True
        # Build graph
        for connection in connections:
            is_reversed = False
            self.graph[connection[1]].append([connection[0], is_reversed])
            is_reversed = True
            self.graph[connection[0]].append([connection[1], is_reversed])
        self.dfs(current_node=0)
        return self.num_reorders

    def dfs(self, current_node: int):
        for idx, (next_node, is_reversed) in enumerate(self.graph[current_node]):
            if not self.visited[next_node]:
                self.visited[next_node] = True
                if is_reversed:
                    self.num_reorders += 1
                    self.graph[current_node][idx][1] = False
                self.dfs(next_node)
        return
