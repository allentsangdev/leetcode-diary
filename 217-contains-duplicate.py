class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = set()
        for x in nums:
            if x in check:
                return True
            else:
                check.add(x)
        return False