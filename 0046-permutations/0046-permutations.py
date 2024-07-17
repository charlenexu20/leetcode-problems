class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # tc: O(n!) | sc: O(n)
        res = []

        def backtracking(used, path):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                # Skip elements that are already used in the current permutation path
                if used[i]: 
                    continue
                
                used[i] = True
                path.append(nums[i])
                backtracking(used, path)
                path.pop()
                used[i] = False

        backtracking([False] * len(nums), [])
        return res