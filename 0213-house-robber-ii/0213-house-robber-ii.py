class Solution:
    def rob(self, nums: List[int]) -> int:
        #DP | tc: O(n) | sc: O(1)

        rob1 = self.helper(nums[1:])
        rob2 = self.helper(nums[:-1])

        # Return the max of the only one house, rob1, or rob2
        return max(nums[0], rob1, rob2)

    # solution from house robber I
    def helper(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            new_rob = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = new_rob

        return rob2