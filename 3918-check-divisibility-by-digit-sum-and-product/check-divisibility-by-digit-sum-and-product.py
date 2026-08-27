class Solution:
    def checkDivisibility(self, n: int) -> bool:
        t = n
        sum = 0
        mul = 1
        while t>0:
            temp  = t%10
            t = t//10
            sum +=temp
            mul = mul * temp
        if n % (sum + mul) == 0:
            return True
        else:
            return False



        