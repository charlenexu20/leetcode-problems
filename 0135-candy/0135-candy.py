class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Greedy | tc: O(n) | sc: O(1)

        # Initialize candy distribution with 1 candy for each child
        candy_array = [1] * len(ratings)

        # Traverse from left to right to ensure right higher rated kids get more candy
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy_array[i] = candy_array[i - 1] + 1
        
        # Traverse from right to left to ensure left higher rated kids get more candy
        for i in range(len(ratings) - 2, - 1, - 1):
            if ratings[i] > ratings[i + 1]:
                candy_array[i] = max(candy_array[i], candy_array[i + 1] + 1)
        
        return sum(candy_array)