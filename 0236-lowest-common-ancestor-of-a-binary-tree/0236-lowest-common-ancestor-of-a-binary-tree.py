# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # post-order DFS

        # Base case
        if not root or root == p or root == q:
            return root

        # Recursively search for the lowest common ancestor in the left subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        # Recursively search for the lowest common ancestor in the right subtree
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        return left if left else right

          