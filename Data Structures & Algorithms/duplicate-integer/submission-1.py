class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_lst = set(nums)
        if len(set_lst) == len(nums):
            return False
        else:
            return True

            
            