class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy | tc: O(n) | sc: O(1)
        cover = 0 # track the farthest index that can be reached

        # already at the last index
        if len(nums) == 1:
            return True

        for i in range(len(nums)):
            # Check if the current index is reachable
            if i <= cover:
                # Update the cover to the maximum reachable index from the current position
                cover = max(i + nums[i], cover)
                # If the cover reaches or exceeds the last index, return True
                if cover >= len(nums) - 1:
                    return True
        return False