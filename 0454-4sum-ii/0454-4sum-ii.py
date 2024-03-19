class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # hashmap | tc: O(n^2) | sc: O(n^2)
        
        hashmap = {} # key: n1+n2 | value: n1+n2 frequency

        for n1 in nums1:
            for n2 in nums2:
                cur_sum = n1 + n2
                hashmap[cur_sum] = hashmap.get(cur_sum, 0) + 1

        count = 0
        for n3 in nums3:
            for n4 in nums4:
                # calculate the complement of the current sum (n3 + n4)
                key = 0 - (n3 + n4)
                # check if the complement exists as a key in the 'hashmap'
                if key in hashmap:
                    # increment by the value associated with the complement key
                    count += hashmap[key]

        return count 