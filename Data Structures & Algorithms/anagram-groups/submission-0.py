class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #determine which strings are same length
        #determine which ones share same characters
        #do this within m * n space complexity
        results = []
        hashed = defaultdict(list)

        for s in strs:
            sorted_word = "".join(sorted(s))
            hashed[sorted_word].append(s)

        return list(hashed.values())

            
