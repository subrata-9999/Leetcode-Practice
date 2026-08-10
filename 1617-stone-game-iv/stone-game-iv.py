class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        memo = {}
        def solve(n:int) -> bool:
            if n ==1:
                return True
            if n in memo:
                return memo[n]
            
            i=1
            while i*i<=n:
                if solve(n-i*i) == False:
                    memo[n] = True
                    return True
                i+=1
            memo[n] = False
            return False
            
        ans = solve(n)
        return ans

        