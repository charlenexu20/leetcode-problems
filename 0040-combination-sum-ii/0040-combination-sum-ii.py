class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # tc: O(2^n)
        res = []
        candidates.sort()

        def backtrack(start_idx, path, total):
            if total == target:
                res.append(path.copy())
                return

            if total > target:
                return

            for i in range(start_idx, len(candidates)):
                # Skip duplicates to avoid redundant combinations
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue

                total += candidates[i]
                path.append(candidates[i])
                backtrack(i + 1, path, total)
                total -= candidates[i]
                path.pop()

        backtrack(0, [], 0)
        return res