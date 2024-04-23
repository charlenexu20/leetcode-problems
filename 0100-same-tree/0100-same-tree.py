# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BFS | tc: O(n) | sc: O(h)
        if not p and not q: return True
        if not p or not q: return False

        # Combine the queues into one queue of tuples (p_node, q_node)
        queue = collections.deque([(p, q)])

        while queue:
            node1, node2 = queue.popleft()
            
            if node1.val != node2.val:
                return False

            # Check the left children
            if node1.left and node2.left:
                queue.append((node1.left, node2.left))
            elif node1.left or node2.left:
                return False

            # Check the right children
            if node1.right and node2.right:
                queue.append((node1.right, node2.right))
            elif node1.right or node2.right:
                return False

        return True

