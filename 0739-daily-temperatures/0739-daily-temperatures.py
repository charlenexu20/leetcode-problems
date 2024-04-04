class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Intuition (two pointers) | tc: O(n) | sc: O(n)
        
        res =[0] * len(temperatures)
        l, r = 0, 1

        while r < len(temperatures):
            # If temperature at r is warmer than at l
            if temperatures[r] > temperatures[l]:
                # update the result for index l
                res[l] = r - l
                l, r = l + 1, l + 1
            else:
                r += 1
                # Update pointers if r reaches end
                if r >= len(temperatures):
                    l, r = l + 1, l + 1

        return res
        