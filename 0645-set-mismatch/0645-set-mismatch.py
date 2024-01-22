class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate, missing = 0, 0
        count = Counter(nums)

        for i in range(1, len(nums) + 1):
            if count[i] == 0:
                missing = i
            if count[i] == 2:
                duplicate = i

        return [duplicate, missing]
