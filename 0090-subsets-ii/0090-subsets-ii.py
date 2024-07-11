class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # tc: O(n * 2^n) | sc: O(n)
        
        res = []
        nums.sort() # Sort nums to handle duplicates properly

        def backtracking(start_idx, path):
            res.append(path.copy())

            for i in range(start_idx, len(nums)):
                # Skip duplicates to avoid redundant subsets
                if i > start_idx and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtracking(i + 1, path)
                path.pop()

        backtracking(0, [])
        return res
        