from typing import List
import math
from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        starting_points = set(tuple(pt) for pt in points)
        points_to_consider = starting_points.copy()
        max_num_pts = 0
        while len(starting_points) != 0:
            slope_dict = defaultdict(list)
            num_pts_dict = defaultdict(int)
            start_pt = starting_points.pop()
            points_to_consider.remove(start_pt)

            for pt in points_to_consider:
                slope = self.findSlope(pt, start_pt)
                if num_pts_dict[slope] == 0:
                    num_pts_dict[slope] += 1
                slope_dict[slope].append(pt)
                num_pts_dict[slope] += 1
            slope_w_most_pts = max(slope_dict, key=num_pts_dict.get)

            if num_pts_dict[slope_w_most_pts] > max_num_pts:
                max_num_pts = num_pts_dict[slope_w_most_pts]

            for pt in slope_dict[slope_w_most_pts]:
                starting_points.discard(pt)
        return max_num_pts

    def findSlope(self, pt1, pt2):
        try:
            slope = (pt1[1] - pt2[1]) / (pt1[0] - pt2[0])
        except ZeroDivisionError:
            slope = "inf"

        return slope


if __name__ == "__main__":
    Sol = Solution()
    print(Sol.maxPoints([[-9, -651], [-4, -4], [-8, -582], [9, 591], [-3, 3]]))
