class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashed = {}
        for i, n in enumerate(nums):
            if n in hashed:
                return True
            else:
                hashed[n] = i
        return False
        