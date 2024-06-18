# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        stack = [(0, len(nums) - 1, None)]  # tuple (left, right, root)
        root = None

        while stack:
            left, right, parent = stack.pop()
            mid = (left + right) // 2   # Calculate the middle index
            node = TreeNode(nums[mid])  # Create a new node with the middle value

            # Set the node as left or right child of the parent based on its value
            if parent:
                if node.val < parent.val:
                    parent.left = node
                else:
                    parent.right = node
            else:
                root = node  # If no parent, set this node as the root

            # Push left and right subproblems onto the stack
            if left <= mid - 1:
                stack.append((left, mid - 1, node))
            if mid + 1 <= right:
                stack.append((mid + 1, right, node))

        return root