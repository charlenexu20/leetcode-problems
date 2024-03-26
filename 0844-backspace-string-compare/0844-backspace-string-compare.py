class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # two-pointers(optimized) | tc: O(n + m) | sc: O(1)

        index_s = len(s) - 1
        index_t = len(t) - 1

        # Iterate through both strings from the end
        while index_s >= 0 or index_t >=0:
            # Find the index of next valid character in each string
            index_s = self.next_valid_index(s, index_s)
            index_t = self.next_valid_index(t, index_t)

            char_s = s[index_s] if index_s >= 0 else ""
            char_t = t[index_t] if index_t >= 0 else ""

            if char_s != char_t:
                return False
            index_s -= 1
            index_t -= 1

        return True

    # Helper function to skip backspaces
    def next_valid_index(self, string, index):
        backspace = 0
        while index >= 0:
            if backspace == 0 and string[index] != "#":
                break
            elif string[index] == "#":
                backspace += 1
            else:
                backspace -= 1
            index -= 1
        return index



        