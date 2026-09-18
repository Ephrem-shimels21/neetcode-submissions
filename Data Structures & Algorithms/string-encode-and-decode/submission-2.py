class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []

        for s in strs:
            result.append(str(len(s)))
            result.append(",")

        result.append("#")

        result.extend(strs)
        return ''.join(result)     
        
    def decode(self, s: str) -> List[str]:
        sizes, res, i = [], [], 0
        while s[i] != "#":
            j = i
            while s[j] != ",":
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        i += 1
        for sz in sizes:
            res.append(s[i: i + sz])
            i += sz
        
        return res


    

    