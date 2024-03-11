class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # hashtable | tc: O(m + n) | sc: O(m)
        
        res = []
        nums1_count = collections.Counter(nums1)

        for n in nums2:
            if nums1_count[n]:
                res.append(n)
                nums1_count[n] -= 1

        return res


        # FOLLOW-UP #1: if the given array is already sorted,  
        # we can optimize the algorithm by using a two-pointer approach.

        # FOLLOW-UP #2: if nums1's size is small compared to nums2's size,
        # using a hash map to store the frequency counts of elements in nums1 
        # and then iterating through nums2 to find the intersection.
        


        

        