class Solution:
    def minimumPushes(self, word: str) -> int:
        # d = {
        #     'x': 1, 'y': 2,
        #     'c': 1, 'd': 2,
        #     'e': 1, 'a': 2, 'b': 3,
        #     'f': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5,
        #     'g': 1, 'o': 2, 'p': 3, 'q': 4,
        #     'h': 1, 'r': 2, 's': 3, 't': 4, 'u': 5,
        #     'i': 1, 'v': 2, 'w': 3, 'z': 4,
        #     'j': 1
        # }
        pointer = 2
        power = 1
        d= {}
        ans = 0
        for i in range(len(word)):
            if word[i] in d:
                ans += d[word[i]]
                continue
            ans+=power
            pointer+=1
            if pointer>9:
                power+=1
                pointer = 2
        return ans
            
            
            


