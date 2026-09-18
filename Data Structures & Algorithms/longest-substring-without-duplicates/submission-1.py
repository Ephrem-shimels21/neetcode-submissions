class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        left = 0
        max_leng = 0

        for right in range(len(s)):

            if s[right] in mp:
                left = max(mp[s[right]] + 1, left)
            
            mp[s[right]] = right
            max_leng = max(max_leng, right - left + 1)
        
        return max_leng



         