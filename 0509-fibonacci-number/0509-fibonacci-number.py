class Solution:
    def fib(self, n: int) -> int:
        # BASE CASE
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        # RECURSIVE CASE
        return self.fib(n - 1) + self.fib(n - 2)

        