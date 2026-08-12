class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i = 0
        dp = {}
        ans = -1
        for j in range(len(nums)):
            if nums[j] in dp:
                dp[nums[j]] +=1
            else:
                dp[nums[j]] = 1
            
            while dp[nums[j]]>k:
                dp[nums[i]] -=1
                i+=1
            ans = max(ans, j-i+1)
        return ans
            

            


        