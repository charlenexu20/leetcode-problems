class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Greedy | tc: O(nlog n) | sc: O(1)
        
        points.sort()
        res = 1

        for i in range(1, len(points)):
            # Check if the current balloon is not overlapping with the previous one
            if points[i][0] > points[i - 1][1]:
                res += 1
            else:
                # Update the right boundary of overlapping balloons 
                # to track the furthest position that can be burst with a single arrow
                points[i][1] = min(points[i - 1][1], points[i][1])

        return res