class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # tc: O(nlogn)
        
        intervals.sort()
        output = [intervals[0]]

        for start, end in intervals[1 : ]:
            # Get the end of the last interval in output
            last_end = output[-1][1]

            if start <= last_end: # Check for overlap
                output[-1][1] = max(last_end, end) # Merge intervals by updating the last end
            else:
                output.append([start, end])

        return output