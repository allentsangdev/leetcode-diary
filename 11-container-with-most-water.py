from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        L,R = 0, len(height)-1
        maxArea = 0
        while L < R:
            # first cal max area
            if (R-L) * min(height[R],height[L]) > maxArea:
                maxArea = (R-L) * min(height[R],height[L])
            # move pointer by comparing which col has lower height
            
            if height[R] > height[L]:
                L += 1
            elif height[R] < height[L]:
                R -= 1
            elif height[R] == height[L]:
                L += 1
        return maxArea