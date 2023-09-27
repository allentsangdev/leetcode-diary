from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1 ):
            if i == 0 and digits[i] == 9:
                digits[i] = 0
                digits.insert(0, 1)
                break
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break

        return digits
            
    def plusOne_lessEfficient(self, digits: List[int]) -> List[int]:
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


