class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # hash table | tc: O(N)
        res = 0
        count = collections.Counter(nums)

        max_frequency = max(count.values())

        for f in count.values():
            if f == max_frequency:
                res += f

        return res

        
        