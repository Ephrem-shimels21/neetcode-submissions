class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, num in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            target = -num
            while left < right:
                if nums[left] + nums[right] == target:
                    curr_ans = [num, nums[left], nums[right]]
                    if curr_ans not in result:
                        result.append(curr_ans)
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
                
        
        return result



        