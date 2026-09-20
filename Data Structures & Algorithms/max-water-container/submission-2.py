class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftP, rightP = 0, len(heights) - 1
        maxC = 0 

        while leftP < rightP:
            minH = min(heights[leftP], heights[rightP])
            maxC = max(maxC, (rightP - leftP)  * minH)

            if heights[leftP] < heights[rightP]:
                leftP += 1
            
            else:
                rightP -= 1
        
        return maxC