class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers | tc: O(n^2) | sc: O(1)
        res = []
        nums.sort()

        for i, v in enumerate(nums):
            # if the current element is > 0, no need to proceed further
            if v > 0:
                return res

            # skip duplicate elements to avoid duplicate triplets
            if i > 0 and v == nums[i - 1]:
                continue

            # initialize two pointers for the remaining elements
            left, right = i + 1, len(nums) - 1

            # use two pointers approach to find the remaining two elements that sum up to zero
            while left < right:
                three_sum = v + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    res.append([v, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # skip duplicate elements to avoid duplicate triplets
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res