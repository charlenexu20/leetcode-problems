class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # stack(optimized) | tc: O(n + m) | sc: O(n + m)

        return self.remove_backspace(s) == self.remove_backspace(t)

    def remove_backspace(self, s):
        stack = []
        for char in s:
            if char != "#":
                stack.append(char)
            elif stack:
                stack.pop()

        return "".join(stack)