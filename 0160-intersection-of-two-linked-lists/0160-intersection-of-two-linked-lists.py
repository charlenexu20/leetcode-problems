# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        It iterates until either l1 or l2 reaches the end of their respective list. 
        When this happens, it resets the pointer to the head of the other list. 
        Continues until either l1 and l2 point to the same node (indicating an intersection) 
        or both become None (indicating no intersection).
        
        tc: O(n + m)
        sc: O(1)
        """

        l1, l2 = headA, headB

        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
            
        return l1