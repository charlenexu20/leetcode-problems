"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if not root:
            return

        res.append(root.val)

        for child in root.children:
            self.dfs(child, res)
        