# doubly linked list

class ListNode:

    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()  # dummy head node
        self.tail = ListNode()  # dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def get(self, index: int) -> int:
        if index >= self.size:
            return - 1

        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node, prev, next = ListNode(val), self.head, self.head.next
        prev.next = new_node
        next.prev = new_node
        new_node.next = next
        new_node.prev = prev

        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node, prev, next = ListNode(val), self.tail.prev, self.tail
        prev.next = new_node
        next.prev = new_node
        new_node.next = next
        new_node.prev = prev

        self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        
        new_node, prev, next = ListNode(val), cur.prev, cur
        prev.next = new_node
        next.prev = new_node
        new_node.next = next
        new_node.prev = prev

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        
        cur = self.head.next
        for _ in range(index):
            cur = cur.next

        cur.prev.next = cur.next
        cur.next.prev = cur.prev

        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)