# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # DFS recursive 
        if not root: 
            return False

        return self.dfs(root, targetSum - root.val)

    def dfs(self, node: TreeNode, remaining_sum: int) -> bool:
        if not node.left and not node.right and remaining_sum == 0:
            return True
        if not node.left and not node.right:
            return False

        if node.left:
            remaining_sum -= node.left.val
            if self.dfs(node.left, remaining_sum):
                return True
            remaining_sum += node.left.val  # backtracking, restore remaining_sum

        if node.right:
            remaining_sum -= node.right.val
            if self.dfs(node.right, remaining_sum):
                return True
            remaining_sum += node.right.val  # backtracking, restore remaining_sum
        
        return False
