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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # BFS(optimized) | TC: O(N) | SC: O(1)
        
        cur = root
        next_level = root.left if root else None

        while cur and next_level:
            # Connect left child of current node to its right child
            cur.left.next = cur.right

            # If current node has a next node, 
            # connect its right child to left child of next node
            if cur.next:
                cur.right.next = cur.next.left

            # Move pointer
            cur = cur.next

            # Update next level start pointer if current level ends
            if not cur:
                cur = next_level
                next_level = cur.left

        return root
        