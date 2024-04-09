class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        For people ahead of k:
        - If they want fewer tickets, count all their tickets.
        - If they want more tickets, count only as many as k need.

        For people behind k:
        - If they want more tickets, count one less than k need, 
        - as k will finish before their last ticket purchase.

        tc: O(n) | sc: O(1)
        """
       
        res = 0
        
        for i in range(len(tickets)):
            if i <= k:
                res += min(tickets[i], tickets[k])
            else:
                res += min(tickets[i], tickets[k] - 1)

        return res

        