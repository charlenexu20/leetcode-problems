class Solution:
    def validPalindrome(self, s: str) -> bool:
        # two pointers | tc: O(n) | sc: O(n)

        left, right = 0, len(s) - 1

        while left < right:
            # If characters at the current pointers don't match
            if s[left] != s[right]:
                # Create two substrings by skipping one character from either side
                skipLeft = s[:left] + s[left + 1:]
                skipRight = s[:right] + s[right + 1:]

                # Check if either of the substrings is a palindrome
                return (skipLeft == skipLeft[::-1] 
                        or skipRight == skipRight[::-1])
                        
            left, right = left + 1, right - 1

        return True
        