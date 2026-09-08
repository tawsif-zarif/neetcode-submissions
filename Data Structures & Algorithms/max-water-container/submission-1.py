class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # initialise tracking variables
        maxA = 0
        left = 0
        right = len(heights) - 1
        # create loop that runs without using negative widths:
        while left < right:
            # calculate area
            width = right - left
            height = min(heights[left], heights[right])
            newA = width * height
            if newA > maxA:
                maxA = newA
            # now code pointer moving logic
            if heights[left] < heights[right]:
                left += 1
            else: 
                right -= 1

        return maxA