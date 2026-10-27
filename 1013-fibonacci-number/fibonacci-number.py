class Solution:
    def fib(self, n: int) -> int:
        dc = {}
        dc[0] = 0
        dc[1] = 1
        def fun(n:int) -> int:
            if n not in dc:
                dc[n] = fun(n-2)+ fun(n-1)
            return dc[n]
        return fun(n)
        