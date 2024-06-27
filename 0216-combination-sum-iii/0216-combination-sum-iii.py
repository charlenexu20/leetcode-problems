class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # tc: O(n * 2^n) | sc: O(n)
        res = []

        def backtrack(start, path, cur_sum):
            if len(path) == k:
                if cur_sum == n:
                    res.append(path.copy())
                return

            for i in range(start, 9 + 1):
                cur_sum += i
                path.append(i)
                backtrack(i + 1, path, cur_sum)
                cur_sum -= i
                path.pop()

        backtrack(1, [], 0)
        return res