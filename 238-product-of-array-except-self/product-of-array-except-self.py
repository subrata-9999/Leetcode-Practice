class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        mul = 1
        count_zero = 0
        non_zero_mul = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                count_zero +=1
            else:
                non_zero_mul *= nums[i]
            mul *=nums[i]
        ans = []

        if count_zero>1:
            return [0]*len(nums)

        for i in range(len(nums)):
            if nums[i] != 0:
                ans.append(mul//nums[i])
            if nums[i] == 0:
                ans.append(non_zero_mul)
        return ans
        