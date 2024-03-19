class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers | tc: O(n) | sc: O(1)
        l, r = 0, len(numbers) - 1
        while l < r:
            current_sum = numbers[l] + numbers[r]
            if current_sum < target:
                l += 1
            elif current_sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]

        