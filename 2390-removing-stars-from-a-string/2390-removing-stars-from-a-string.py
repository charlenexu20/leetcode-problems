class Solution:
    def removeStars(self, s: str) -> str:
        # (Revised) stack | tc: O(n) | sc: O(n)
        
        stack = []

        for char in s:
            if char == "*":
                stack and stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
