class Solution:
    def toLowerCase(self, s: str) -> str:
        """
        converts uppercase characters in the input string 
        to their lowercase equivalents using ASCII values

        tc: O(n) | sc: O(n)
        """

        s = list(s)
        for i in range(len(s)):
            ascii_val = ord(s[i])
            if 65 <= ascii_val <= 90 :
                s[i] = chr(ascii_val + 32)

        return "".join(s)

        