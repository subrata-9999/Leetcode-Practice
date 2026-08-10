class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = {}
        def solve(n: int) -> bool:
            if n < 0:
                return False
            if n in dp:
                return dp[n]
            i = 1
            while i**2 <= n:
                if solve(n-i**2)==False:
                    dp[n] = True
                    return True
                i+=1
            dp[n] = False
            return False
        return solve(n)

        