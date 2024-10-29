class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP | tc: O(n) | sc: O(1)

        # Two variables to store max money up to two previous houses
        rob1, rob2 = 0, 0

        for n in nums:
            # Calculate the max money if we rob this house (n + rob1) or skip it (rob2)
            tmp = max(n + rob1, rob2)
            # rob1 now holds the previous max (old rob2),
            rob1 = rob2
            # rob2 holds the current max (new tmp)
            rob2 = tmp

        return rob2