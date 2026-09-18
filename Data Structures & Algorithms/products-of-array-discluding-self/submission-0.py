class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward_move, backward_move = [nums[0]], [0] * len(nums)
        backward_move[len(nums) - 1] = nums[-1]

        for idx in range(1, len(nums)):
            forward_move.append(forward_move[idx -1] * nums[idx])
        
        for idx in range(len(nums) - 2, 0, -1):
            backward_move[idx] = backward_move[idx + 1] * nums[idx]

        result = []

        for i in range(len(nums)):
            if i == 0:
                result.append(backward_move[i + 1])
            elif i == len(nums) - 1:
                result.append(forward_move[i -1])
            else:
                result.append(forward_move[i - 1] * backward_move[i + 1])

        return result


        