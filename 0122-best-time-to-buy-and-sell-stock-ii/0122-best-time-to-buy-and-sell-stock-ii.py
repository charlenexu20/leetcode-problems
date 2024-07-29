class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Greedy | tc: O(n) | sc: O(1)
        res = 0

        for i in range(1, len(prices)):
            res += max(prices[i] - prices[i - 1], 0)

        return res