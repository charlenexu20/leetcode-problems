class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy | tc: O(N) | sc: O(1)
        res = 0
        l = r = 0 # window for the current jump range

        while r < len(nums) - 1:
            farthest = 0 # farthest index that can be reached in this jump
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest
            res += 1

        return res 