class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashed = set()
        for i in nums:
            if i in hashed:
                return True
            else:
                hashed.add(i)
        return False