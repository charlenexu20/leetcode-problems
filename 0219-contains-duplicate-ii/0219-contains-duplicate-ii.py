class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """    
        Sliding window approach:
        - We maintain a set 'window' to keep track of elements within the sliding window.
        - Use two pointers 'i' and 'j' to represent the left and right boundaries of the window.
        - While expanding the window (j), if the window size exceeds 'k', remove the leftmost element from the window.
        - If the current element 'nums[j]' is already in the window, return True (duplicate found).
        - Otherwise, add the current element 'nums[j]' to the window and move both pointers forward.
        - If no duplicates are found after iterating through the entire array, return False.

        Time complexity: O(N), where N is the length of the input array nums.
        Space complexity: O(k), where k is the size of the sliding window.
        """

        window = set()
        i, j = 0, 0

        while j < len(nums):
            if j - i > k:
                window.remove(nums[i])
                i += 1

            if nums[j] in window:
                return True
            window.add(nums[j])
            j += 1
        
        return False


