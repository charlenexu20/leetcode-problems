# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # DFS recursive | tc: O(n) | sc: O(h)
        
        return self.compare(root.left, root.right)

    
    def compare(self, left, right):
        # elminate null and different vals
        if not left and not right: return True
        elif not left or not right: return False
        elif left.val != right.val: return False

        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        return outside and inside

