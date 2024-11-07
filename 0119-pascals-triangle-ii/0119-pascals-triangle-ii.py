class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # tc: O(rowIndex^2) | sc: O(rowIndex)
        
        # Start with the first row, which is always [1]
        res = [1]

        # Build each row up to the specified rowIndex
        for i in range(rowIndex):
            next_row = [0] * (len(res) + 1)

            # Compute each value in the next row based on the previous row
            for j in range(len(res)):
                next_row[j] += res[j]
                next_row[j + 1] += res[j]
            
            res = next_row
        return res