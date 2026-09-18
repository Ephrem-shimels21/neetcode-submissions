class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward_move, backward_move = [0] * len(nums),  [0] * len(nums)
        backward_move[len(nums) - 1] = 1
        forward_move[0] = 1


        for i in range(1, len(nums)):
            forward_move[i] = forward_move[i -1] * nums[i - 1]
        
        for j in range(len(nums) - 2, -1, -1):
            backward_move[j] = backward_move[j + 1] * nums[j + 1]
        
        res = []

        for i in range(len(nums)):
            res.append(forward_move[i] * backward_move[i])
        

        return res
        