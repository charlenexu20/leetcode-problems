class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            l, r = 0, len(word) - 1
            while word[l] == word[r]:
                if l >= r:
                    return word
                l, r = l + 1, r - 1
        return ""
