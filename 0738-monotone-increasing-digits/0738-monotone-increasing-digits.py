class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # Greedy | tc: O(n) | sc: O(n)
    
        str_num = str(n)
        flag = len(str_num)

        for i in range(len(str_num) - 1, 0, - 1):
            # If the current digit is smaller than the previous one
            if str_num[i - 1] > str_num[i]:
                flag = i
                # Decrease the previous digit
                str_num = str_num[:i - 1] + str(int(str_num[i - 1]) - 1) + str_num[i:]
        
        # Set all digits after the flag to '9'
        for i in range(flag, len(str_num)):
            str_num = str_num[:i] + "9" + str_num[i + 1:]

        return int(str_num)