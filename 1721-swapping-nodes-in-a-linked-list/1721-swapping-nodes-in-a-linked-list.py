# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # brute force | tc: O(N)| sc: O(N)

        nodes_array = []
        cur = head

        # traverse the linked list and store the elements in an array
        while cur:
            val = cur.val
            nodes_array.append(val)
            cur = cur.next

        # swap the required elements by indexing the array
        n = len(nodes_array)
        nodes_array[k - 1], nodes_array[n - k] = nodes_array[n - k], nodes_array[k - 1]

        # rebuild the linked list using the order of the elements in the array
        dummy_head = ListNode()
        cur = dummy_head
        for val in nodes_array:
            node = ListNode(val)
            cur.next = node
            cur = cur.next
        cur.next = None

        return dummy_head.next
