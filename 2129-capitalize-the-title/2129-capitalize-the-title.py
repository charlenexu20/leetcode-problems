class Solution:
    def capitalizeTitle(self, title: str) -> str:
        # tc: O(n) | sc: O(n)

        words = title.split()
        res = []

        for word in words:
            if len(word) <= 2:
                res.append(word.lower())
            else:
                res.append(word.capitalize())

        return " ".join(res)


        