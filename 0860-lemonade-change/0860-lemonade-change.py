class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Greedy | tc: O(n) | sc:O(1)

        five, ten = 0, 0

        for bill in bills:
            # Condition 1
            if bill == 5:
                five += 1

            # Condition 2
            if bill == 10:
                if five <= 0:
                    return False
                five -= 1
                ten += 1

            # Condition 3
            if bill == 20:
                # Try use $10 bill for change
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1    
                # Then use three $5 bills for change 
                elif five >= 3:
                    five -= 3       
                else:
                    return False

        return True