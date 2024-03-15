# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        two pointers(Hare-Tortoise) | tc: O(n) | sc: O(1)

        Cycle Detection: use the Floyd's Tortoise and Hare algorithm to 
        detect whether a cycle exists in the linked list. 
        If the two pointers meet at some point, we know there's a cycle.

        Find the start of the cycle: when there's a prefix before the cycle, 
        the start of the cycle shifts backward by the length of the prefix. 
        To find the start of the cycle, we need to advance one pointer 
        to the head of the list and move both pointers simultaneously until they meet again. 
        This meeting point will be the start of the cycle.
        """

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # check if there's a cycle
            if slow == fast:
                # set one of the pointers back to head
                slow = head

                # look for the node where the cycle begins
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None

