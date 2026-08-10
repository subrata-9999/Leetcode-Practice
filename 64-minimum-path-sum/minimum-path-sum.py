class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        dp = {}
        m = len(grid)
        n = len(grid[0])
        def solve(m1: int, n1: int)->int:
            if (m1,n1) in dp:
                return dp[(m1,n1)]

            if m1==m-1 and n1==n-1:
                return grid[m1][n1]
            
            if m1==m-1 and n1!=n-1:
                dp[(m1,n1)] = grid[m1][n1] + solve(m1, n1+1)
            elif m1!=m-1 and n1==n-1:
                dp[(m1,n1)] = grid[m1][n1] + solve(m1+1, n1)
            else:
                dp[(m1,n1)] = min(grid[m1][n1] + solve(m1+1, n1), grid[m1][n1] + solve(m1, n1+1))
            return dp[(m1,n1)]


        return solve(0,0)

            
            
                
                


        