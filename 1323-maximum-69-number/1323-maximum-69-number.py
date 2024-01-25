class Solution:
    def maximum69Number (self, num: int) -> int:
        num_arr = [digit for digit in str(num)]
        
        for i in range(len(num_arr)):
            # Change the first occurrence of 6 to 9
            if num_arr[i] == "6":
                num_arr[i] = "9"
                break

        return int("".join(num_arr))

        