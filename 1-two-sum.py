from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hash map for the list of integers
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        
        # search for the number that can add up to target
        for i in range(len(nums)):
            searchTarget = target - nums[i]
            firstIndex = i
            if searchTarget in hashMap:
                secondIndex = hashMap[searchTarget]
                if secondIndex != i:
                    return [firstIndex, secondIndex]

        # return false if no valid result
        return False

numberList = [2,7,11,15]
targetNumber = 9
solution = Solution()
result = solution.twoSum(numberList,targetNumber)
print(result)