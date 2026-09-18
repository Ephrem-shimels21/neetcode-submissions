class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_counter = Counter(t)
        s_counter = Counter(s)

        return t_counter == s_counter

       
        
        