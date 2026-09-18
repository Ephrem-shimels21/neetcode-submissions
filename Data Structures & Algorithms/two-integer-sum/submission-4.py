class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq_count = {}

        for indx, num in enumerate(nums):
            diff = target - num
            
            if diff in freq_count:
                return [freq_count[diff], indx]
                
            freq_count[num] = indx
        

            
            



        