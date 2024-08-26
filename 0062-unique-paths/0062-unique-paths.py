class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP | tc: O(m x n) | sc: O(m x n)

        # Create a 2D DP array with dimensions m x n initialized to 0
        dp = [[0] * n for _ in range(m)]

        # Initialize the first column to 1 (only one way to reach any cell in the first column)
        for i in range(m):
            dp[i][0] = 1

        # Initialize the first row to 1 (only one way to reach any cell in the first row)
        for j in range(n):
            dp[0][j] = 1

        # Fill the DP table using the recurrence relation
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        # The answer is in the bottom-right corner of the grid
        return dp[m - 1][n - 1]