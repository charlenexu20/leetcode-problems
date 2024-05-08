# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS inorder iterative | tc: O(n) | sc: O(h)

        stack = []
        cur = root
        prev = float("-inf")

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left  # left
            
            cur = stack.pop()  # mid

            # Check if the current node violates the BST property
            if prev >= cur.val:
                return False
            
            prev = cur.val
            cur = cur.right  # right

        return True
        
        


