class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1
        
        #sorts by highest value
        value = sorted(counts, key=counts.get, reverse=True)[:k]

        return value

        









        
