class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # tc: O(n * 2^n) | sc: O(n)
        res = []

        def backtracking(start_idx, path):
            if len(path) > 1:
                res.append(path.copy())
            
            # Array to track used elements in the current recursion level
            used = [0] * 201 # Using an array for tracking numbers from -100 to 100
            for i in range(start_idx, len(nums)):
                # Conditions to skip duplicates or elements that violate the increasing order
                if (path and nums[i] < path[-1]) or used[nums[i] + 100] == 1:
                    continue
                
                # Mark nums[i] as used in the current recursion level
                used[nums[i] + 100] = 1
                path.append(nums[i])
                backtracking(i + 1, path)
                path.pop()

        backtracking(0, [])
        return res