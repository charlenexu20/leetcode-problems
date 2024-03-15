# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # tc: O(n) | sc: O(n)

        visited = set()
        cur = head
        prev = None

        while cur:
            if cur.val in visited:
                prev.next = cur.next
            else:
                visited.add(cur.val)
                prev = cur
            cur = cur.next

        return head