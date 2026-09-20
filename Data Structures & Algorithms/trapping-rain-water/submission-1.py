class Solution:
    def trap(self, height: List[int]) -> int:
        maxC = 0
        n = len(height)
        leftMaxes = [0] * len(height)
        rightMaxes = [0] * len(height)

        leftMaxes[0] = height[0]

        for i in range(1, n):
            leftMaxes[i] = max(leftMaxes[i - 1], height[i])
        
        rightMaxes[n - 1] = height[n - 1]

        for i in range(n - 2, -1, -1):
            rightMaxes[i] = max(rightMaxes[i + 1], height[i])
        
        
        for i in range(n):
            maxC += min(leftMaxes[i], rightMaxes[i]) - height[i]
        
        return maxC
        
        
        




