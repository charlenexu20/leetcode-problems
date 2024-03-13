# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iteration | tc: O(N) | sc: O(1)
        dummy_head = ListNode(0, head)
        cur = dummy_head

        while cur.next and cur.next.next:
            # store pointers to the nodes to be swapped
            node1 = cur.next
            node2 = cur.next.next

            # swap the nodes
            node1.next = node2.next
            node2.next = node1
            cur.next = node2

            # move to the next pair of nodes
            cur = node1

        return dummy_head.next


