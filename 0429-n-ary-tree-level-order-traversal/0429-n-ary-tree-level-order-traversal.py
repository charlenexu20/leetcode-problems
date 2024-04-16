"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        #BFS | TC: 0(N) | SC: O(N)
        
        if not root: return []
        queue = collections.deque([root])
        res = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                for child in node.children:
                    queue.append(child)

            res.append(level)
        return res
        