class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_5 = 0
        count_10 = 0

        for bill in bills:
            if bill == 5:
                count_5 += 1
            elif bill == 10 and count_5:
                count_10 += 1
                count_5 -= 1   
            elif bill == 20 and (count_5 and count_10) or count_5 >= 3:
                if count_5 and count_10:
                    count_5 -= 1
                    count_10 -= 1
                else:
                    count_5 -= 3
            else: return False

        return True

