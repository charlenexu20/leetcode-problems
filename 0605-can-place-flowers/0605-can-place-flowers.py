class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # add 0 to the beginning and at the end of the array
        f = [0] + flowerbed + [0]

        # iterate through the array but skip the first and last index
        for i in range(1, len(f) - 1):
            # check if three continuous spots empty
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0: 
                f[i] = 1
                n -= 1

        return n <= 0