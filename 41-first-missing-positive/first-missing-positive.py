class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()
        dic = {}
        for i in range(len(nums)):
            if nums[i] <1:
                continue
            dic[nums[i]] = nums[i]-1
        for i in range(len(nums)):
            if i + 1 not in dic:
                return i+1
                
        return nums[len(nums)-1]+1