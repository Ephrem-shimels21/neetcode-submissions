class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, frq in count.items():
            freq[frq].append(num)
        
        res = []
        for indx in range(len(freq) - 1, 0, -1):
            for num in freq[indx]:
                res.append(num)
                if len(res) == k:
                    return res
        



        