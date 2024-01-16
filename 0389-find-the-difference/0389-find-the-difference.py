class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0: return t

        s_count = {}
        for i in s:
            s_count[i] = s_count.get(i, 0) + 1

        for j in t:
            if j in s_count and s_count[j] > 0: 
                s_count[j] -= 1
            else:
                return j
        