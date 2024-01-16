class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words): 
            return False

        letter_to_word = {}
        word_to_letter = {}
        
        for l, w in zip(pattern, words):
            # CHECK FOR ONE-TO-ONE RELATIONSHIP
            if l in letter_to_word and letter_to_word[l] != w:
                return False
            if w in word_to_letter and word_to_letter[w] != l:
                return False
            letter_to_word[l] = w
            word_to_letter[w] = l
        return True
        