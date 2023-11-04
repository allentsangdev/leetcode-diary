from typing import List

class Solution:
    # O(n)2 implemenation
    def inefficient_dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []
        
        for i in range(len(temperatures)):
            count = 1
            if i != len(temperatures) - 1:
                for j in range(i+1,len(temperatures)):
                    remainingElement = len(temperatures) - (i+1)
                    if temperatures[j] > temperatures[i]:
                        answer.append(count)
                        break
                    else:
                        count += 1
                        if count > remainingElement:
                            answer.append(0)
                            break
            else:
                answer.append(0)
        
        return answer
    
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        stack = []

        for index, temp in enumerate(temps):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = (index - stackIndex)
            stack.append([temp, index])
        return res

# Test Cases
temperatures = [73,74,75,71,69,72,76,73]
solution = Solution()
x = solution.inefficient_dailyTemperatures(temperatures)

y = solution.dailyTemperatures(temperatures)

print(y)