class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_in.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
        

    def peek(self) -> int:
        """
        Get the front element without modifying the state of the stack.
        """
        res = self.pop()
        self.stack_out.append(res)
        return res
        

    def empty(self) -> bool:
        """
        Evaluates to False if either of the stacks contains any elements
        """
        return not (self.stack_in or self.stack_out)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()