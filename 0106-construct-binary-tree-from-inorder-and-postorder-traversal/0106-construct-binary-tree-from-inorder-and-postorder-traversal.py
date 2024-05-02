# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # step 1: base case check
        if not inorder or not postorder: return None
        
        # Step 2: the last val in postorder is the root
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # Step 3: find the deliminator index
        delimiter_idx = inorder.index(root_val)

        # Step 4: separate the inorder array into left and right
        inorder_left = inorder[ : delimiter_idx]
        inorder_right = inorder[delimiter_idx + 1 : ]

        # Step 5: separate the postorder array into left and right
        postorder_left = postorder[ : len(inorder_left)]
        postorder_right = postorder[len(inorder_left) : len(postorder) - 1]
    
        # Step 6: Recursion
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root

