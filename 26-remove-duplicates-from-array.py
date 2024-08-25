class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Left pointer gonna tell us where to put the next unique value
        # Right pointer gonna traverse the list
        L = 1
        for R in range(1, len(nums)):
            if R != len(nums):
                if nums[R] != nums[R - 1]:
                    nums[L] = nums[R]
                    L += 1
        return L
