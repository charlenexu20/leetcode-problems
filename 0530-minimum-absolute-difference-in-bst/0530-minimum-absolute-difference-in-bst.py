# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # DFS inorder recursive
        
        if not root:
            return 0

        self.arr = []

        self.inorder(root)
        res = float('inf')

        for i in range(1, len(self.arr)):
            # calculate the min diff of an ordered array
            res = min(res, self.arr[i] - self.arr[i - 1])

        return res

    def inorder(self, root):
        if not root:
            return
        
        self.inorder(root.left)
        self.arr.append(root.val) # convert to ordered array
        self.inorder(root.right)