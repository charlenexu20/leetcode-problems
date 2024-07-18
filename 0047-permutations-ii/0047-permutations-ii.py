class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # tc: O(n! * n) | sc: O(n)
        res = []
        nums.sort()

        def backtracking(used, path):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]: 
                    continue
                
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtracking(used, path)
                    path.pop()
                    used[i] = False

        backtracking([False] * len(nums), [])
        return res