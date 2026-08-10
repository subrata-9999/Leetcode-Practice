class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = {}
        def solve(m1: int, n1:int) -> int:
            if (m1,n1) in dp:
                return dp[(m1,n1)]

            if m1==m-1 and n1==n-1:
                return 1

            if m1== m-1 and n1!= n-1:
                dp[(m1,n1)] = solve(m1, n1+1)
            elif m1!=m-1 and n1==n-1:
                dp[(m1,n1)] = solve(m1+1, n1)
            else:
                dp[(m1, n1)] = solve(m1+1, n1) + solve(m1, n1+1)
            return dp[(m1,n1)]

        return solve(0, 0)

        