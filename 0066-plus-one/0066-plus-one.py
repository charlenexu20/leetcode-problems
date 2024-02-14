class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, - 1, - 1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the current digit is 9, set it to 0 and continue to the next digit
            digits[i] = 0
        # If all digits are 9, add a new leading 1 to the list
        return [1] + digits
        