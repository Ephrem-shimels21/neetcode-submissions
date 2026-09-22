class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_dict = {}
        leftP = rightP = 0
        long_subs = 0

        while rightP < len(s):
            while s[rightP] in sub_dict:
                sub_dict[s[leftP]] -= 1
                if sub_dict[s[leftP]] == 0:
                    sub_dict.pop(s[leftP])
                leftP += 1
            
            sub_dict[s[rightP]] = 1 + sub_dict.get(s[rightP], 0)
            long_subs = max(long_subs, rightP - leftP + 1)
            rightP += 1
        
        return long_subs




       


         