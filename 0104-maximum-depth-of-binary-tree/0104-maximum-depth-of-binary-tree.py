# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS recursive | tc: O(n) | sc: O(n)
        
        if not root: return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        depth = 1 + max(left_depth, right_depth)

        return depth