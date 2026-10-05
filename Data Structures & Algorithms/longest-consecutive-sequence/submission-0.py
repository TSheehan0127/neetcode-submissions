class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0
        
        for n in nums:
            #check if its the start of a sequence
            if (n - 1) not in unique:
                length = 0
                while (n + length) in unique:
                    length += 1
                longest = max(length, longest)
        return longest