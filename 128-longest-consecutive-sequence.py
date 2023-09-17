from typing import List

# edge cases
# 1. if there is duplicated number
# 2. can not use sort algorithmes 
# 3. if nums is a empty list

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        # cast to number list to a set to make sure there is no duplicated number
        numSet = set(nums)
        longest = 1
        for num in numSet:
            # if a number is the start of a sequence
            if num - 1 not in numSet:
                nextIndex = 1
                while num + nextIndex in numSet:
                    nextIndex += 1
                if nextIndex > longest:
                    longest = nextIndex
        
        return longest