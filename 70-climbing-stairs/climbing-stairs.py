class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[1] = 1
        memo[2] = 2
        def solve(n: int) -> int:
            if n in memo:
                return memo[n]
            memo[n] = solve(n-1) + solve(n-2)
            return memo[n]
        return solve(n)

        