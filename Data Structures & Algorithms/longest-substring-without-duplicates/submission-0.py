class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        pointer = 0
        max_len = 0

        for indx,letter in enumerate(s):

            while letter in store:
                store.remove(s[pointer])
                pointer += 1
                max_len = max(max_len, indx - pointer + 1)
                
            store.add(letter)
            max_len = max(max_len, indx - pointer + 1)

        
        return max_len
            




         