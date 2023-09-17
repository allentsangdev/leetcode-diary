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

        sequenceLength = []
        # check if a number is a start of a sequence
        for num in nums:
            # if a number is not the start of a sequence, continue
            if num - 1 in numSet:
                continue
            # if a number is the start of a sequence
            elif num - 1 not in numSet:
                # process to check if num + nextIndex exisit
                nextIndex = 1
                while num + nextIndex in numSet:
                    nextIndex += 1
                sequenceLength.append(nextIndex)
        
        return max(sequenceLength)