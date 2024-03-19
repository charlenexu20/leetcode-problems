class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # two pointers | tc: O(n^3) | sc: O(1)
        length = len(nums)
        if length < 4:
            return []

        res = []
        nums.sort()

        for i in range(length):
            # avoid duplicate quadruplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
        
            for j in range(i + 1, length):
                # avoid duplicate quadruplets
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, length - 1
                while left < right:
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if four_sum < target:
                        left += 1
                    elif four_sum > target:
                        right -= 1
                    else:
                        # add the quadruplet to the result
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -=1

                        # avoid duplicate quadruplets
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return res
        