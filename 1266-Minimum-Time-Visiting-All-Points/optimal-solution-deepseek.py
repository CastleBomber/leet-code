#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date: March 7th, 2026
    Purpose: Prepping for coding test

    LeetCode: #1266 Minimum Time Visiting All Points

    On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi].
    Return the minimum time in seconds to visit all the points in the order given by points.

    You can move according to these rules:
    - move vertically by one unit (1 sec)
    - move horizontally by one unit (1 sec)
    - move diagonally (1 sec for both horizontal and vertical change)

    Example 1:
        Input: points = [[1,1],[3,4],[-1,0]]
        Output: 7

    Example 2:
        Input: points = [[3,2],[-2,2]]
        Output: 5

    Constraints:
        points.length == n
        1 <= n <= 100
        points[i].length == 2
        -1000 <= points[i][0], points[i][1] <= 1000

    Usage:
        python3 optimal-solution-deepseek.py

    Notes:
        For each consecutive pair (x1,y1) → (x2,y2), the minimum time is
        max(|x2-x1|, |y2-y1|) because diagonal moves cover both axes simultaneously.
        Sum over all consecutive pairs.

    TIME AND SPACE COMPLEXITY: Chebyshev Distance Summation
    ----------------------------------------------------
    Metric           | Complexity | Reason
    ----------------------------------------------------
    Time Complexity  | O(n)       | Single pass through the n points, computing
                                    constant-time operations per adjacent pair.
                                    
    Space Complexity | O(1)       | Only a few integer variables (total_time, dx, dy, i)
                                    used; no additional data structures scale with input.
    ----------------------------------------------------

*********************************************************
"""

from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0

        # Iterate through consecutive point pairs
        for i in range(1, len(points)):
            x1, y1 = points[i-1]
            x2, y2 = points[i]

            # Chebyshev distane: max of absolute differences
            dx = abs(x2 -x1)
            dy = abs(y2 - y1)
            total_time += max(dx, dy)

        return total_time


if __name__ == "__main__":
    # Test cases – note: points are given as lists of lists, not strings
    points1 = [[1,1], [3,4], [-1,0]]
    points2 = [[3,2], [-2,2]]
    
    sol = Solution()
    print(sol.minTimeToVisitAllPoints(points1))  # Expected: 7
    print(sol.minTimeToVisitAllPoints(points2))  # Expected: 5