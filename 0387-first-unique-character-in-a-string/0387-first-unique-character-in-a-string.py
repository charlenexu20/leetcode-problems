class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)

        for l in s:
            count[l] += 1

        for i, v in enumerate(s):
            if count[v] == 1:
                return i
                
        return - 1
        