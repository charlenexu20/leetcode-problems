class Solution:
    def fib(self, n: int) -> int:
        # Base case
        if n < 2:
            return n

        # Initialize the dp array
        dp = [0, 1]

        for _ in range(2, n + 1):
            curr = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = curr

        return dp[1] 