class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}

        for word in strs:
            word_sorted = sorted(word)
            word_key = "".join(word_sorted)
            if word_key in strs_dict:
                strs_dict[word_key].append(word)
            else:
                strs_dict[word_key] = [word]
        
        return [value for value in strs_dict.values()]