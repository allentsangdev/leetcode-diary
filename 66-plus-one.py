from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ''
        for i in digits:
            number = number + str(i)
        
        number = int(number) + 1

        res =[]
        for i in str(number):
            res.append(int(i))
        
        return res

digits = [1,2,3]
solution = Solution()
print(solution.plusOne(digits))


