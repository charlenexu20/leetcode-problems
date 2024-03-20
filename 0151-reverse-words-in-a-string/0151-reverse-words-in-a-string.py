class Solution:
    def reverseWords(self, s: str) -> str:
        # Two pointers (w/o built-in) | tc: O(n) | sc: O(n)

        # Trim leading and trailing spaces
        left, right = 0, len(s) - 1
        while left <= right and s[left] == " ":
            left += 1
        while left <= right and s[right] == " ":
            right -= 1

        # Process the words in the reversed order
        start = end = right
        reversed_words = []

        while start >= left:
            # Find end of current word
            while start >= left and s[start] != " ":
                start -= 1
            # Extract and append word
            reversed_words.append(s[start + 1 : end + 1])

            # Find start of next word
            while start >= left and s[start] == " ":
                start -= 1
            end = start

        return " ".join(reversed_words)

        
            
        """
        Solutions with built-in functions
        - The split() method automatically handles 
            - leading and trailing whitespace characters 
            - when splitting a string into a list of substrings
        """

        # s = s.split()
        # res = []

        # for i in range(len(s) - 1, - 1, - 1):
        #     res.append(s[i])

        # return " ".join(res)


        # s = s.split()
        # left, right = 0, len(s) - 1
        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1

        # return " ".join(s)


        