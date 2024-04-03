class MinStack:

    def __init__(self):
        self.stack = [] # Main stack to store elements
        self.min_stack = [] # Stack to store minimum elements at each position
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Update the minimum value stack
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)
        

    def pop(self) -> None:
        # Pop the top element from both stacks
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()