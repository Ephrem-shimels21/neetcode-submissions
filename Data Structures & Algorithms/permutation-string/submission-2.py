class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        
        l, r = 0, len(s1) - 1
        s1_dict = Counter(s1)

        while r < len(s2):
            if Counter(s2[l : r + 1]) == s1_dict:
                return True
            r += 1
            l += 1
        
        return False

