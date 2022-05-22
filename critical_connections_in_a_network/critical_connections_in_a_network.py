from typing import List
from itertools import repeat


class Solution:
    """Referenced from https://www.youtube.com/watch?v=Rhxs4k6DyMM"""

    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        self.graph = [[] for _ in range(n)]
        self.bridges = []
        self.parent = list(repeat(-1, n))
        self.discovery_time = list(repeat(-1, n))
        self.lowest_reachable = list(repeat(-1, n))
        self.time = 0
        for edge in connections:
            self.add_edge(edge)
        start_node = 0

        self.dfs(start_node)
        return self.bridges

    def dfs(self, u: int):
        self.discovery_time[u] = self.lowest_reachable[u] = self.time
        self.time += 1

        for v in self.graph[u]:
            if self.discovery_time[v] == -1:
                self.parent[v] = u
                self.dfs(v)
                self.lowest_reachable[u] = min(
                    self.lowest_reachable[u], self.lowest_reachable[v]
                )

                if self.lowest_reachable[v] > self.discovery_time[u]:
                    self.bridges.append([u, v])

            elif v != self.parent[u]:
                # Ignore child to parent edge
                self.lowest_reachable[u] = min(
                    self.lowest_reachable[u], self.discovery_time[v]
                )

    def add_edge(self, edge: tuple):
        self.graph[edge[0]].append(edge[1])
        self.graph[edge[1]].append(edge[0])


if __name__ == "__main__":
    Sol = Solution()
    input_list = [[0, 1], [1, 2], [2, 0], [1, 3]]
    n = len(input_list)
    print(Sol.criticalConnections(n, input_list))
