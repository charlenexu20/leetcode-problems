class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # sliding window | tc: O(N) | sc: 0(1)

        # initial window and the maximum sum
        window_sum = sum(nums[ : k])
        max_sum = window_sum

        # iterate from the (k)th element to the end of the array
        for i in range(k, len(nums)):
            # subtract the left element of the window
            # add the right element of the window
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k
        