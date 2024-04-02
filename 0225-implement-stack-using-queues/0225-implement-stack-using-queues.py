class MyStack:

    def __init__(self):
        self.queue = deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)


    def pop(self) -> int:
        # Move each element except the last one to the end
        for i in range(len(self.queue) - 1):
            self.push(self.queue.popleft())
        # The last element in the queue is the one to be removed and returned
        return self.queue.popleft()
        

    def top(self) -> int:
        return self.queue[-1]
        

    def empty(self) -> bool:
        return not self.queue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()