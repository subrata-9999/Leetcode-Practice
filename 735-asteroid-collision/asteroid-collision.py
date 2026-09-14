class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = len(asteroids)-1
        while i>=0:
            if not stack:
                stack.append(asteroids[i])
                i-=1
            else:
                if (stack[-1]<0 and asteroids[i]>0):
                    if abs(stack[-1])<abs(asteroids[i]):
                        stack.pop()
                    elif abs(stack[-1])==abs(asteroids[i]):
                        stack.pop()
                        i-=1
                    elif abs(stack[-1])>abs(asteroids[i]):
                        i-=1
                else:
                    stack.append(asteroids[i])
                    i-=1
        return stack[::-1]
                    




        