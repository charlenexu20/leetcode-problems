# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     # recursion | tc: O(N) | sc: O(N)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head, None)
    
    def reverse(self, cur, prev):
        # base case
        if not cur:
            return prev

        # store the next node before modifying `next` pointer of current node
        next = cur.next

        # reverse `next` pointer of current node to point to previous node
        cur.next = prev

        # recursively call function with next node as cur and cur node as prev
        return self.reverse(next, cur)
