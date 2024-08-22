class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # DP | tc: O(n) | sc: O(n)

        # Initialize dp array to account for the step beyond the last one
        dp = [0] * (len(cost) + 1)
        dp[0] = 0   # No cost to start
        dp[1] = 0   # No cost to start


        for i in range(2, len(cost) + 1):
            # Recurrence relation
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[-1]