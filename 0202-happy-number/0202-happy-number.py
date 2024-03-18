class Solution:
    def isHappy(self, n: int) -> bool:
        """
        converts the number to a string, iterates over its digits, 
        and computes the sum of squares.
        """
        visited = set()

        while n not in visited:
            visited.add(n)
            n = sum((int(digit) ** 2) for digit in str(n))

            if n == 1:
                return True

        return False