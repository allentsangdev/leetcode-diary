from typing import List
class Solution:    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0:
                if nums[i] == nums[i-1]:
                    continue
            
            L,R = i + 1, len(nums) - 1

            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    result.append([nums[i],nums[L],nums[R]])
                    L += 1
                    while nums[L] == nums[L-1] and L < R:
                        L += 1
                if nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
                if nums[i] + nums[L] + nums[R] < 0:
                    L += 1
        
        return result