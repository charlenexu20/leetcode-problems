class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if abs(target) > total_sum or (target + total_sum) % 2 == 1:
            return 0

        target_sum = (target + total_sum) // 2
        dp = [0] * (target_sum + 1)
        dp[0] = 1

        for num in nums:
            for j in range(target_sum, num - 1, - 1):
                dp[j] += dp[j - num]

        return dp[target_sum]