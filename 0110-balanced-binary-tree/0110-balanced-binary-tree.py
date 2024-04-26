# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # DFS recursive | tc: O(n) | sc: O(h)
        return self.dfs(root)[0]

    def dfs(self, node):
        # Return a pair of values: [a boolean, the height of the tree]
        if not node: return [True, 0]

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        # Calculate the balance status of the current subtree
        balanced = (
            left[0] and right[0] and
            abs(left[1] - right[1]) <= 1
        )

        # Calculate the height of the current subtree
        height = max(left[1], right[1]) + 1

        return [balanced, height]

