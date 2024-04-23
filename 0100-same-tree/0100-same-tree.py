# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS | tc: O(n) | sc: O(h)

        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        # Recursively check if the left and right subtrees are the same
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))
