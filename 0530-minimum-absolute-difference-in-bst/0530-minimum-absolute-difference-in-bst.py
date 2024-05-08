# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # DFS inorder iterative

        stack = []
        cur = root
        prev = None
        res = float('inf')

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()

            if prev:
                res = min(res, cur.val - prev.val)
            prev = cur
            cur = cur.right

        return res