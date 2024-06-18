# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursive (reverse inorder) | tc: O(n) | sc: O(h)

        cur_sum = 0

        def dfs(node):
            if not node:
                return

            nonlocal cur_sum

            # reverse in-order traversal
            dfs(node.right) # traverse right subtree
            # update node value with accumulated sum of all greater nodes
            tmp = node.val
            node.val += cur_sum
            cur_sum += tmp # update cur_sum after processing current node
            dfs(node.left) # traverse left subtree

        dfs(root)
        return root