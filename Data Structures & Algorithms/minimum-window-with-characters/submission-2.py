class Solution:
    def minWindow(self, s: str, t: str) -> str:

        countT, window = {}, {}
        res, resLen = [-1, -1], float('inf')

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        windowCount, requiredCount = 0, len(countT)

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                windowCount += 1
            
            while windowCount == requiredCount:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    windowCount -= 1
                
                l += 1 
        
        l, r = res

        return s[l : r + 1] if resLen != float('inf') else ""
            







        