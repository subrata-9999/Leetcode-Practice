class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        nums.sort(reverse=True)
        half = 0
        if len(nums) %2 == 0:
            half = len(nums)//2
        else:
            half = (len(nums)//2) + 1
        print(nums)
        ans = 0
        for i in range(half):
            ans += nums[i]**2
        for i in range(half, len(nums)):
            ans -= nums[i]**2
        return ans
            


        