"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # BFS(optimized) | TC: O(N) | SC: O(1)
        
        if not root: return root
        leftmost = root

        while leftmost:
            cur = leftmost
            leftmost = None
            prev = None

            # Process the current level
            while cur:
                if cur.left:
                    if not leftmost:
                        leftmost = cur.left
                    
                    if prev:
                        prev.next = cur.left
                    prev = cur.left

                if cur.right:
                    if not leftmost:
                        leftmost = cur.right

                    if prev:
                        prev.next = cur.right
                    prev = cur.right

                cur = cur.next

        return root
        