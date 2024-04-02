class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # stack | tc: O(n) | sc: O(n)

        stack = [] # [letter, count]

        for letter in s:
            # If the current letter matches the letter at the top of the stack
            if stack and stack[-1][0] == letter:
                # Increment the count
                stack[-1][1] += 1
            else:
                # Append a new list to the stack representing the current letter and its count (1)
                stack.append([letter, 1])

            # If the count reaches k, remove k consecutive duplicates
            if stack[-1][-1] == k:
                stack.pop()

        # Reconstruct the string without duplicates
        res = ""
        for letter, count in stack:
            res += letter * count

        return res

            

        