class Solution:
    def climbStairs(self, n: int) -> int:
        # DP | tc: O(n) | sc: O(n)

        if n <= 1:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        # Fill the DP array for steps from 3 to n
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]