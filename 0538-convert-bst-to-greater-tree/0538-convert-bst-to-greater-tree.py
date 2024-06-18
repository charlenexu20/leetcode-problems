# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # iterative (reverse inorder) | tc: O(n)

        if not root:
            return None

        stack = []
        cur_sum = 0
        cur = root

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur_sum += cur.val
                cur.val = cur_sum
                cur = cur.left

        return root