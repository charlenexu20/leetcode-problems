# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # DFS optimized | TC: O(log N * log N) | SC: O(log N)
        
        if not root: return 0

        left, right = root.left, root.right
        left_depth, right_depth = 1, 1

        # Get left depth
        while left:
            left_depth += 1
            left = left.left

        # Get right depth
        while right:
            right_depth += 1
            right = right.right

        # If it's a perfect tree
        if left_depth == right_depth:
            return (2 ** left_depth) - 1  # Subtracting 1 accounts for the root node

        # If it's not a perfect tree, recursively count nodes in the left and right subtrees
        return self.countNodes(root.left) + self.countNodes(root.right) + 1  # Add 1 for the root node


