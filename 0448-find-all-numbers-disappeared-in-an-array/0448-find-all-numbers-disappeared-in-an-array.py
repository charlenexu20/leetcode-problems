class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # cyclic sort | tc: O(N) | sc: O(1)

        # Cyclic sort to arrange the numbers at their correct indices
        i = 0
        while i < len(nums):
            # Get the correct index for the current number
            correct_idx = nums[i] - 1
            if nums[i] != nums[correct_idx]:
                # Swap elements
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                # Move to the next element if the current one is already at the correct position
                i += 1
            
        # Find missing numbers
        missing = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                missing.append(i + 1)
        
        return missing