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

# Test Cases
temperatures = [73,74,75,71,69,72,76,73]
solution = Solution()
x = solution.inefficient_dailyTemperatures(temperatures)