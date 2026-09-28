class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashed = {}
        for i, e in enumerate(nums):
            if target - e in hashed:
                return [hashed[target - e], i]
            else:
                hashed[e] = i
