class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashtable | tc: O(m * n) |
        res = defaultdict(list) # charCount : list of Anagram
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # convert the array to tuple because lists can't be used as keys
            res[tuple(count)].append(s)

        return res.values()
             

        
        