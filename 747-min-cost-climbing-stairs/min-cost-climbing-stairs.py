class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def solve(n:int) -> int:
            if n in dp:
                return dp[n]
            if n>=len(cost):
                return 0
            
            take = cost[n] + solve(n+1)
            skip = cost[n] + solve(n+2)
            final_take = min(take, skip)
            dp[n] = final_take

            return dp[n]

        return min(solve(0), solve(1))

        