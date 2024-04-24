# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # DFS | tc: O(s * t) | sc: O(h)
        if not subRoot: return True
        if not root: return False

        if self.isIdentical(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))

    def isIdentical(self, s, t):
        if not s and not t:
            return True

        if s and t and s.val == t.val:
            return (self.isIdentical(s.left, t.left) and
                    self.isIdentical(s.right, t.right))
        
        # If either tree is empty or their values are not equal
        return False

        