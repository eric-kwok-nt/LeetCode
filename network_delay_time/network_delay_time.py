import heapq
import math
from itertools import repeat
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        k -= 1
        self.adj_mat = [[] for _ in range(n)]
        self.convertToAdjMat(times)
        visited = list(repeat(False, n))
        dist = list(repeat(math.inf, n))
        dist[k] = 0
        H = [(dist[k], k)]

        while H:
            dist_u, u = heapq.heappop(H)
            if not visited[u]:
                visited[u] = True
                for v, t in self.adj_mat[u]:
                    if dist[v] > dist_u + t:
                        dist[v] = dist_u + t
                        heapq.heappush(H, (dist[v], v))
        max_dist = max(dist)
        if max_dist == math.inf:
            return -1
        return max_dist

    def convertToAdjMat(self, times: List[List[int]]):
        for time in times:
            u = time[0] - 1
            v = time[1] - 1
            t = time[2]
            self.adj_mat[u].append((v, t))
