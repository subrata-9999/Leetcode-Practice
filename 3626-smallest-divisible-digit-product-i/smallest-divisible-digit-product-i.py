class Solution:
        
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_multiple(m: int, u: int) -> int:

            multiple = 1
            while m>0:
                temp = m%10
                multiple *= temp
                m = m//10

            if multiple%u == 0:
                return True
            else:
                return False
        for i in range(n, n+10):
            if digit_multiple(i, t) == True:
                return i
            



        