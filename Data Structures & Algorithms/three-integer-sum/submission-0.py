class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []

        for i in range(len(nums) - 2):
            # skip duplicate "target" values to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]  # we want nums[l] + nums[r] == -nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                current_sum = nums[l] + nums[r]
                if current_sum > target:
                    r -= 1
                elif current_sum < target:
                    l += 1
                else:
                    answer.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip duplicates for l and r too
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return answer