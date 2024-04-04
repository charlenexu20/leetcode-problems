class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic decreasing stack | tc: O(n) | sc: O(n)
        
        res =[0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for idx, temp in enumerate(temperatures):
            # Check if stack is not empty and current temp is warmer than the temp at the top of the stack
            while stack and temp > stack[-1][0]:
                # Pop temperature and index from stack
                stack_temp, stack_idx = stack.pop()
                # Calculate days until warmer temperature
                res[stack_idx] = idx - stack_idx
            # Append current temperature and index pair to stack
            stack.append([temp, idx])

        return res
        