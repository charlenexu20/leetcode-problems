class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # DP | tc: O(n x m) | sc: O(n x m)

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        dp = [[0] * n for _ in range(m)]

        # Fill the first column
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break

        # Fill the first row 
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break
        
        # Fill the rest of the DP table, skipping cells with obstacles
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
        