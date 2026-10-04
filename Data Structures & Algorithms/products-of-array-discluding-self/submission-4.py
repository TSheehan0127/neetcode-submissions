class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        product = 1
        has_zero = False
        has_zeros = False

        for i in nums:
            if i != 0:
                product *= i
            elif has_zero:
                has_zeros = True
            else:
                has_zero = True

        for i in range(len(nums)):
            if has_zeros:
                answer.append(0)
            elif nums[i] == 0:
                answer.append(product)
            elif has_zero:
                answer.append(0)
            else:
                answer.append(product // nums[i])

        return answer