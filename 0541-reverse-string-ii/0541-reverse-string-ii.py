class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # two pointers | tc: O(n) | sc: O(n)

        s_list = list(s)
        n = len(s_list)

        # Iterate the arr in intervals of 2k
        for i in range(0, n, 2 * k):
            # Ensure the calculated indices stay in-bound
            start = i
            end = min(i + k - 1, n - 1)

            while start < end:
                # Reverse the characters in-place
                s_list[start], s_list[end] = s_list[end], s_list[start]
                start += 1
                end -= 1

        return "".join(s_list)




        