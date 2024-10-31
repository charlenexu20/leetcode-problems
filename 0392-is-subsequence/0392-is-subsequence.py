class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #two pointers | tc: O(n) | sc: O(1)

        i, j = 0, 0

        # Loop until we reach the end of either string
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        # If i has reached the end of s, it means s is a subsequence of t
        return i == len(s)