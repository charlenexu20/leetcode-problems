class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # If the sum is odd, partitioning is impossible
        if sum(nums) % 2 == 1:
            return False

        # Calculate target (half of the total sum)
        target = sum(nums) // 2

        # Initialize DP array
        dp = [0] * (target + 1)

        # Iterate through each number in nums
        for n in nums:
            # Update DP array from right to left (to avoid overwriting values)
            for j in range(target, n - 1, - 1):
                dp[j] = max(dp[j], dp[j - n] + n)

        return dp[-1] == target