class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # Greedy | tc: O(n) | sc: O(1)
        if len(nums) <= 1:
            return len(nums)

        res = 1
        cur_diff = 0
        prev_diff = 0

        for i in range(len(nums) - 1):
            cur_diff = nums[i + 1] - nums[i]
            # Check if the current difference indicates a change in wiggle direction
            if (
                (prev_diff <= 0 and cur_diff > 0) or # Previous was non-positive and current is positive
                (prev_diff >= 0 and cur_diff < 0)    # Previous was non-negative and current is negative
            ):
                res += 1
                prev_diff = cur_diff

        return res
        