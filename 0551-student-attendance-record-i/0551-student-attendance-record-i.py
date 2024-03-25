class Solution:
    def checkRecord(self, s: str) -> bool:
        # iterate over the characters and keep separate counts for 'A's and 'L's
        # tc: O(n) | sc: O(1)

        absent = 0
        late = 0

        for char in s:
            if char == "A":
                absent += 1
                if absent == 2:
                    return False
            
            if char == "L":
                late += 1
                if late > 2:
                    return False

            else:
                late = 0

        return True

        