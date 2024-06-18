# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildBST(left: int, right:int) -> Optional[TreeNode]:
            # Base case:
            if left > right:
                return None

            # Choose the middle element as the root for currrent subtree
            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            # Recursively build left and right subtrees
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)

            return root

        return buildBST(0, len(nums) - 1)