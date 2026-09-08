class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = []

        leftMax = 0
        for i in range(len(height)):
            maxLeft.append(leftMax)
            leftMax = max(leftMax, height[i])

        rightMax = 0
        for n in range(len(height) - 1, -1, -1):
            maxRight.append(rightMax)
            rightMax = max(rightMax, height[n])

        maxRight = list(reversed(maxRight))

        total_water = 0

        for m in range(len(height)):
            if min(maxLeft[m], maxRight[m]) - height[m] > 0:
                total_water += min(maxLeft[m], maxRight[m]) - height[m]

        return total_water