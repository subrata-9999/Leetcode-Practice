class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        s = list(s)
        feq = {}
        l = 0
        max_len = -1


        for i in range(len(s)):
            if s[i] in feq:
                feq[s[i]] += 1
            else:
                feq[s[i]] = 1
            while feq[s[i]]>2:
                feq[s[l]] -= 1
                l += 1
            max_len = max(max_len , i - l + 1)
        return max_len


        