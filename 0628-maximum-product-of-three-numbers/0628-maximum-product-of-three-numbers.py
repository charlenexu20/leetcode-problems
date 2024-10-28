class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Sorting | tc: O(nlogn) | sc: O(1)

        nums.sort()
        
        # Product of three largest numbers
        product_1 = nums[-1] * nums[-2] * nums[-3]
        # Product of two smallest and one largest 
        product_2 = nums[0] * nums[1] * nums[-1]
            
        return max(product_1, product_2)