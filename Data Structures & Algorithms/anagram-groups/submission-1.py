class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = defaultdict(list)

        for word in strs:
            word_sorted = sorted(word)
            word_key = "".join(word_sorted)
            strs_dict[word_key].append(word)
        
        return list(strs_dict.values())