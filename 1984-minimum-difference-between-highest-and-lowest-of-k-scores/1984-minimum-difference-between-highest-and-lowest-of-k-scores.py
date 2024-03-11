class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # sliding window | tc: O(nlogn) | sc: O(1)
        
        nums.sort()
        i, j = 0, k - 1
        res = float('inf')
        
        while j < len(nums):
            res = min(res, nums[j] - nums[i])
            i += 1
            j += 1

        return res

        