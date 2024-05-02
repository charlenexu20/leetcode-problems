# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Recursion | tc: O(n*log(n))
        -keep dividing the array into two halves from the current node 
        and create left and right subtree accordingly
        """

        if not nums: return None

        max_val = max(nums)
        root = TreeNode(max_val)
        mid_idx = nums.index(max_val)

        root.left = self.constructMaximumBinaryTree(nums[ : mid_idx])
        root.right = self.constructMaximumBinaryTree(nums[mid_idx + 1 : ])

        return root