# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # recursion with BST
        
        self.count = 0 # Count of the current value
        self.max_count = 0 # Maximum count of any value found so far
        self.prev = None  # Previous node value in the in-order traversal
        self.res = [] # List to store the mode(s)

        self.searchBST(root)
        return self.res

    def searchBST(self, cur):
        if not cur: return

        # Traverse the left subtree
        self.searchBST(cur.left)

        # Process the current node
        if not self.prev:
            self.count = 1
        elif self.prev.val == cur.val:
            self.count += 1
        else:
            self.count = 1
        self.prev = cur

        if self.count == self.max_count:
            self.res.append(cur.val)
        if self.count > self.max_count:
            self.max_count = self.count
            self.res = [cur.val]
            
        # Traverse the right subtree
        self.searchBST(cur.right)
