class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        l, r = 0, k - 1
        res = []
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i],i))


        while r < len(nums):
            currM, idx = heapq.heappop(heap)

            while idx < l:
                currM, idx = heapq.heappop(heap)

            res.append(-currM)
            l += 1
            r += 1
            if idx >= l:
                heapq.heappush(heap, (currM, idx))

            if r < len(nums):
                heapq.heappush(heap, (-nums[r],r))
            
        return res

        