"""
implementation of a hashmap using chaining for collision resolution
"""

class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 10000
        # Create an array of ListNode objects to store key-value pairs
        self.map = [ListNode() for _ in range(self.size)]

    def hash(self, key):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]
        # Update the value if the key already exists
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        # Insert a new node at the end of the linked list
        cur.next = ListNode(key, value)        

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return - 1

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)