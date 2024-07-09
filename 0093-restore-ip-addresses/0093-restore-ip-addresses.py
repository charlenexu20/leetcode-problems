class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # tc: O(3^4) | sc: O(n)

        res = []

        if len(s) > 12:
            return res

        def backtracking(start_idx, path):
            if len(path) > 4:
                return
            if len(path) == 4 and start_idx == len(s):
                res.append(".".join(path))
                return

            # Explore substrings from start_idx to the end of s
            for j in range(start_idx, len(s)):
                substr = s[start_idx:j + 1]
                if len(substr) > 3 or int(substr) > 255:
                    break
                # Check for leading zeros in a segment longer than one character
                if len(substr) > 1 and substr[0] == "0":
                    break
                path.append(substr)
                backtracking(j + 1, path)
                path.pop()
        
        backtracking(0, [])
        return res