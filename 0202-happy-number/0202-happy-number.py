class Solution:
    def isHappy(self, n: int) -> bool:
        # hashset | tc: O(logn) | sc: O(logn)

        # keep track of visited numbers to detect cycles
        visited = set()

        # loop until encounter 1 or enter a cycle
        while n not in visited:
            visited.add(n)
            n = self.sum_of_squares(n)

            if n == 1:
                return True

        return False

    def sum_of_squares(self, n: int) -> int:
        total = 0
        
        # loop until n becomes 0
        while n:
            # extract the last digit of n
            digit = n % 10
            digit = digit ** 2
            total += digit
            # remove the last digit from n
            n = n // 10

        return total
        