class Solution:
    def integerBreak(self, n: int) -> int:
        # DP | tc: O(n^2) | sc: O(n)

        # Create a DP array to store max product res from 0 to n
        dp = [0] * (n + 1)
        dp[2] = 1  # Base case

        # Iterate over all integers from 3 to n
        for i in range(3, n + 1):
            # For each integer i, try all possible splits j (where 1 <= j <= i // 2)
            for j in range(1, i // 2 + 1):
                # Calculate the maximum product by either:
                # 1) Splitting i into j and (i - j) without further breaking (i - j)
                # 2) Splitting i into j and (i - j) where (i - j) is optimally broken down
                dp[i] = max(dp[i], (i - j) * j, dp[i - j] * j)

        return dp[n]