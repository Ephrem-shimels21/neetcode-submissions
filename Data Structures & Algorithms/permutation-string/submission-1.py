class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, len(s1) - 1
        s1_set = Counter(s1)

        while right < len(s2):
            sub_str = s2[left:right + 1]
            if Counter(sub_str) == s1_set:
                return True
            left += 1
            right += 1
        
        return False
        