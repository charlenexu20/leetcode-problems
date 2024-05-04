# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # If one of the roots is None, return the other root
        if not root1: return root2
        if not root2: return root1

        queue = collections.deque([root1, root2])

        # Process nodes level by level
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()

            # Process left children if present in both trees
            if node1.left and node2.left:
                queue.append(node1.left)
                queue.append(node2.left)
            
             # Process right children if present in both trees
            if node1.right and node2.right:
                queue.append(node1.right)
                queue.append(node2.right)

            # Merge node values
            node1.val += node2.val

            # If node1 has no left child but node2 has one, merge them
            if not node1.left and node2.left:
                node1.left = node2.left
            # If node1 has no right child but node2 has one, merge them
            if not node1.right and node2.right:
                node1.right = node2.right

        # The merged tree is rooted at root1
        return root1

