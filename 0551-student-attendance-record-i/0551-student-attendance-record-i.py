class Solution:
    def checkRecord(self, s: str) -> bool:
        # directly check for the 'A's and consecutive 'L's
        # tc: O(n) | sc: O(1)

        absent = 0

        for i in range(len(s)):
            if s[i] == "A":
                absent += 1
                if absent == 2:
                    return False

            elif i >= 2 and s[i] == s[i-1] == s[i-2] == "L":
                return False

        return True

        