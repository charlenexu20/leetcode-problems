class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # Case 1: The new interval is before the current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i : ]
            # Case 2: The new interval is after the current interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # Case 3: The new interval overlaps with the current interval
            else:
                # Merge the new interval with the current interval
                newInterval = [
                    min(newInterval[0], intervals[i][0]), 
                    max(newInterval[1], intervals[i][1])
                ]

        # Add the last merged interval to the result
        res.append(newInterval)

        return res
        