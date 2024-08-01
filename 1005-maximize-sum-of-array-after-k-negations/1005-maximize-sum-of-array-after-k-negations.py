class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # Greedy | tc: O(nlogn) | sc: O(1)
        
        # Sort the array by absolute values in descending order
        nums.sort(key=abs, reverse=True)

        # Negate negative numbers while K is available
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1

        # If K is still > 0, negate the smallest absolute value
        while k > 0:
            nums[-1] = -nums[-1]
            k -= 1

        return sum(nums)