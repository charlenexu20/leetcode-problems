class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(start_idx, path):
            # Base Case
            if start_idx >= len(s):
                res.append(path.copy())
                return

            for i in range(start_idx, len(s)):
                if self.isPalindrome(s, start_idx, i):
                    path.append(s[start_idx : i + 1])
                    backtrack(i + 1, path)
                    path.pop()
                    
        backtrack(0, [])
        return res

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
