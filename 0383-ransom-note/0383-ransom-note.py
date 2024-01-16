class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_count = {}

        for char in magazine:
            m_count[char] = m_count.get(char, 0) + 1

        for char in ransomNote:
            if char not in m_count or m_count[char] == 0:
                return False
            m_count[char] -= 1
        return True

        