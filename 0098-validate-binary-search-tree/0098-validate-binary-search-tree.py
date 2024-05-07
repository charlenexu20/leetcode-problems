# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS recursive | tc: O(n) | sc: O(h)
        
        def valid(node, left, right):
            # Base case: If the node is None, it's a valid BST
            if not node:
                return True
            
            # Check if the current node's value is within the valid range
            if not (node.val < right and node.val > left):
                return False

            left = valid(node.left, left, node.val)
            right = valid(node.right, node.val, right)
            
            return left and right

        return valid(root, float("-inf"), float("inf"))


