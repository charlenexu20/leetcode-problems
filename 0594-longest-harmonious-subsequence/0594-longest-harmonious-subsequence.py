class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # sliding window | tc: O(nlogn) | sc: O(1)

        res = 0
        nums.sort()
        n = len(nums)
        i, j = 0, 1

        while j < n:
            if nums[j] - nums[i] == 1:
                cur_length = j - i + 1
                res = max(res, cur_length)
                j += 1
            elif nums[j] - nums[i] > 1:
                i += 1
            else:
                j += 1

        return res

        # hashmap | tc: O(n) | sc: O(n)

        res = 0
        count = collections.Counter(nums)

        for num in count:
            if num + 1 in count:
                res = max(res, count[num] + count[num + 1])

        return res