class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def solve(n: int) -> int:
            if n >= len(nums):
                return 0
            if n in memo:
                return memo[n]

            take = nums[n] + solve(n+2)
            skip = solve(n+1)

            memo[n] = max(take, skip)
            return memo[n]
        return solve(0)
            


        