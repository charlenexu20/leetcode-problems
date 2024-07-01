class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # tc: o(n * 4^n)

        # Mapping of digits to their corresponding characters
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def backtrack(i, cur_str):
            # Base case: If cur_str matches the length of digits, add to res
            if len(cur_str) == len(digits):
                res.append(cur_str)
                return

            # Get characters corresponding to the current digit
            digit = digits[i]
            characters = digit_to_char[digit]

            # Iterate through each character and recursively call backtrack
            for c in characters:
                backtrack(i + 1, cur_str + c)

        if digits:
            backtrack(0, "")

        return res