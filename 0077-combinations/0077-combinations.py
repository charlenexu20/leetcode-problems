class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # tc: O(n * 2^n) | sc: O(n)

        res = []

        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return

            for i in range(start, n + 1):
                comb.append(i) # Choose number i to include in the current combination
                backtrack(i + 1, comb) # Recursively generate combinations starting from i + 1
                comb.pop() # Backtrack by removing number i from the current combination

        backtrack(1, [])
        return res