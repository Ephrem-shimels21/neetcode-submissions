class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftP, rightP = 0, len(numbers) - 1

        while leftP < rightP:
            if numbers[leftP] + numbers[rightP] > target:
                rightP -= 1
            
            elif numbers[leftP] + numbers[rightP] < target:
                leftP += 1
            
            else:
                return [leftP + 1 , rightP + 1]