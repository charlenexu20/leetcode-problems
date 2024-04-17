"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # BFS | TC: O(N) | SC: O(N)
        
        if not root: return 0
        queue = collections.deque([root])
        depth = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                for child in node.children:
                    queue.append(child)

            depth += 1
        
        return depth