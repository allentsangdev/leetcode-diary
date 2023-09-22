from typing import List
class Solution:
    def trap_inefficient(self, height: List[int]) -> int:
        result = 0

        # pointer to point to the max of Left and Right
        L,R = 0, len(height) - 1
        
        for i in range(len(height)):
            if i == 0 or i == len(height) - 1:
                continue
            else:
                for j in range(i):
                    if height[j] > height[L]:
                        L = j
                for e in range(len(height)-1, i, -1):
                    if height[e] > height[R]:
                        R = e

                trap = min(height[L], height[R]) - height[i]
                
                if trap > 0:
                    result += trap
                    
        return result