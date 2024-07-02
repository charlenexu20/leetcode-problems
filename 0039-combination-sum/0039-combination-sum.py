class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # tc: O(n * 2^n) | sc: O(target)
        res = []

        def backtrack(start_idx, cur_sum, path):
            # If cur_sum matches the target, add the current path to the res
            if cur_sum == target:
                res.append(path.copy())
                return
            # If cur_sum exceeds the target, stop further exploration for this path
            if cur_sum > target:
                return

            for i in range(start_idx, len(candidates)):
                cur_sum += candidates[i]
                path.append(candidates[i])
                backtrack(i, cur_sum, path)  # Recursively backtrack with updated sum and path
                cur_sum -= candidates[i]  # Backtrack: Remove current candidate from the sum
                path.pop()  # Backtrack: Remove current candidate from the path

        backtrack(0, 0, [])
        return res