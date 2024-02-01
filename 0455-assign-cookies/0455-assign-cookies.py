class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # prioritize using larger cookies for children with higher greed factors.

        g.sort() # Sort the children's greed factor
        s.sort() # Sort the cookies sizes

        index = len(s) - 1 # The index to the last cookie in the sorted list
        res = 0 # The count of satisfied children

        for i in range(len(g) - 1, - 1, - 1):
            # Check if there are available cookies and the current cookie size is sufficient
            if index >= 0 and s[index] >= g[i]:
                res += 1
                index -= 1
        
        return res