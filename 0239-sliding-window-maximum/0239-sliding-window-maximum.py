class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Monotonic decreasing queue | tc: O(n) | sc: O((n)
        # The front of the deque (queue[0]) always holds 
            # the index of the maximum value within the current window.

        res = []
        queue = collections.deque() # store indices of elements
        l = r = 0 # represent the window

        while r < len(nums):
            # Pop indices of smaller values from queue
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            # Add the current index 'r' to the deque
            queue.append(r)

            # Pop indices that fall out of the window range from the front of the deque
            if l > queue[0]:
                queue.popleft()

            # Append the max value to the res when the window size is reached
            if (r + 1) >= k:
                res.append(nums[queue[0]])
                l += 1
            r += 1

        return res
       