class Solution:
    def minimumPushes(self, word: str) -> int:
        d = {}
        for i in range(len(word)):
            if word[i] in d:
                d[word[i]] += 1
            else:
                d[word[i]] = 1
        sorted_data = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        pointer = 2
        power = 1
        ans = 0
        for name, score in sorted_data.items():
            ans += (score*power)
            pointer+=1
            if pointer>9:
                power+=1
                pointer = 2
        
        return ans
        