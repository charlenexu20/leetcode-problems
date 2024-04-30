# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # DFS preorder iterative | tc: O(n) | sc: O(h)

        if not root: return 0
        stack = [root]
        res = 0

        while stack:
            node = stack.pop()
            if node.left and not node.left.left and not node.left.right:
                res += node.left.val
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res

        
        