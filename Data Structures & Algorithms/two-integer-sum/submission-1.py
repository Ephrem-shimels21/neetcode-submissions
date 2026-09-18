class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for ind,num in enumerate(nums):
            diff = target - num
            if diff in store:
                return [store[diff], ind]
            
            store[num] = ind

            
            



        