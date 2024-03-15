class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # hashtable | tc: O(n) | sc: O(1)

        if len(ransomNote) > len(magazine):
            return False

        # index = letter | value = count
        record = [0] * 26

        for letter in magazine:
            record[ord(letter) - ord('a')] += 1

        for letter in ransomNote:
            record[ord(letter) - ord('a')] -= 1
            if record[ord(letter) - ord('a')] < 0:
                return False
        return True

        