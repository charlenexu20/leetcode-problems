class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # tc: O(n * 2^n) | sc: O(n)
        res = []

        def backtracking(start_idx, path):
            res.append(path.copy())

            for i in range(start_idx, len(nums)):
                path.append(nums[i])
                backtracking(i + 1, path)
                path.pop()

        backtracking(0, [])
        return res