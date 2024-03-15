class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashtable | tc: O(n) | sc: O(1)

        if len(s) != len(t):
            return False
            
        # use array as a simple form of a hash table
        record = [0] * 26

        for char in s:
            # calculate the index of the char in the array (0-25)
            record[ord(char) - ord('a')] += 1

        for char in t:
            record[ord(char) - ord('a')] -= 1

        for count in record:
            if count != 0:
                return False
        return True
        