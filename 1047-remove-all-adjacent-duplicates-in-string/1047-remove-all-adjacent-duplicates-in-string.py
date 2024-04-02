class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        This approach effectively removes consecutive duplicates by 
        only keeping one occurrence of each letter while traversing the string. 
        The stack serves as a temporary storage to track the non-duplicate letters encountered so far.

        tc: O(n) | sc: O(n)
        """

        stack = []

        for letter in s:
            if stack and stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)

        return "".join(stack)
        