class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashed = {}
        summ = []
        for i,e in enumerate(nums):
            hashed[e] = i

        for i,e in enumerate(nums):
            if target - e in nums and hashed[target - e] != i:
                return [i, hashed[target - e]]

