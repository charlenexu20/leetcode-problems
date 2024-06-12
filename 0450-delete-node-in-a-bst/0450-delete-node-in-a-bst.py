# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # recursive | tc: O(h)

        # base case
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:  # Node to delete found
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:  # Node has two children
                # Find the in-order successor (smallest node in the right subtree)
                cur = root.right
                while cur.left:
                    cur = cur.left
                # Replace the current node's value with the successor's value
                root.val = cur.val
                # Recursively delete the successor node from the right subtree
                root.right = self.deleteNode(root.right, cur.val)

        return root
