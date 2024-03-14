# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Two pointers (refractored)
        Get the lengths and start at the same length
        
        tc: O(n + m)
        sc: O(1)
        """

        # find lengths of the two linked lists
        lenA = self.get_length(headA)
        lenB = self.get_length(headB)
        
        # adjust the starting pointers to have the same length
        if lenA > lenB:
            headA = self.move_pointer(headA, lenA - lenB)

        if lenB > lenA:
            headB = self.move_pointer(headB, lenB - lenA)

        # traverse both linked lists until intersection or null
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next


    def get_length(self, node):
        """
        calculate the length of a linked list.
        """
        length = 0
        while node:
            length += 1
            node = node.next
        return length


    def move_pointer(self, node, length):
        """
        move the pointer forward by a specified length.
        """
        while length:
            node = node.next
            length -= 1
        return node