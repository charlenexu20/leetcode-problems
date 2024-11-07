class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # tc: O(n^2)
        
        # The first row of Pascal's triangle is always [1]
        res = [[1]]

        # Outer loop to build each row of Pascal's triangle
        for i in range(1, numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                # Each element is the sum of the two elements directly above it in the previous row
                row[j] = res[i - 1][j - 1] + res[i - 1][j]

            res.append(row)

        return res