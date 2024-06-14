# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # dfs recursive | tc: O(n) | sc: O(h)

        if not root:
            return None

        # If current node's val is less than low, trim left subtree
        if root.val < low:
            return self.trimBST(root.right, low, high)

        # If current node's val is greater than high, trim right subtree
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        # If current node's val is within the range, recursively trim left and right subtrees
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        # Return the modified root of the trimmed BST
        return root