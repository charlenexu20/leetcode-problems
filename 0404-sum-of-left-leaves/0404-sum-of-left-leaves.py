# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # DFS inorder recursive | tc: O(n) | sc: O(h)

        if not root: return 0
        if not root.left and not root.right: return 0

        left_value = self.sumOfLeftLeaves(root.left)
        # Check if the left child exists and is a leaf node
        if root.left and not root.left.left and not root.left.right:
            left_value = root.left.val

        right_value = self.sumOfLeftLeaves(root.right)

        res = left_value + right_value

        return res
        