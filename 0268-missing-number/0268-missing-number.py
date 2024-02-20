class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        # Calculate the sum of numbers from 0 to n
        total_sum = n * (n + 1) // 2

        # Calculate the sum of numbers in the input list
        nums_sum = sum(nums)

        # Find the missing number
        return total_sum - nums_sum
        