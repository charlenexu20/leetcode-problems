class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # DP | tc: O(n) | sc: O(1)
        res = max(nums)
        cur_min, cur_max = 1, 1

        for n in nums:
            # reset them to 1 to start fresh after encountering a 0
            if n == 0:
                cur_min, cur_max = 1, 1
                continue

            # Store the current maximum before updating it
            tmp_max = cur_max
            cur_max = max(cur_max * n, cur_min * n, n)
            cur_min = min(tmp_max * n, cur_min * n, n)
            res = max(res, cur_max)

        return res