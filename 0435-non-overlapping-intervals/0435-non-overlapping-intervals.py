class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Greedy | tc: O(nlog n)
        
        intervals.sort()
        res = 0

        for i in range(1, len(intervals)):
            # Check for overlapping intervals
            if intervals[i][0] < intervals[i - 1][1]:
                # Update the right boundary of the current interval 
                # to the minimum of its own and prev interval right boundary
                intervals[i][1] = min(intervals[i - 1][1], intervals[i][1])
                res += 1

        return res