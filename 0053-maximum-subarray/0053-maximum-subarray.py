class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Greedy | tc: O(n) | sc: O(1)
        res = float('-inf')
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum > res:
                res = cur_sum
            
            # If the current sum becomes non-positive, reset it to 0
            # A negative sum would not contribute to a maximum subarray
            if cur_sum <= 0:
                cur_sum = 0
        
        return res

