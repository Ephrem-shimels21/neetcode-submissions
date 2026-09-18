class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict()

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        

        freq_count = []
        for num in counter.keys():
            freq_count.append([counter[num], num])
        
        freq_count.sort()
        res = []
        idx = len(freq_count) - 1
        while k > 0:
            res.append(freq_count[idx][1])
            k -= 1
            idx -= 1
        
        return res


        