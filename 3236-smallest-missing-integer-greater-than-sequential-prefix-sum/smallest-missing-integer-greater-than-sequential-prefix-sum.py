class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seq_len = 1
        seq_sum = nums[0]
        dp = {}
        target = -1
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]+1:
                seq_len+=1
                seq_sum+=nums[i]
            else:
                break
        target = seq_sum

        j = 0
        while j<len(nums):
            if nums[j] == target:
                target+=1
                j=0
            j+=1
        return target

        
