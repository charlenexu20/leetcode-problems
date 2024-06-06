# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: 
            return root

        # If both are less than the current root, search left subtree
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # If both are greater than the current root, search right subtree
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # If neither of the above conditions is met, root is the LCA
        return root