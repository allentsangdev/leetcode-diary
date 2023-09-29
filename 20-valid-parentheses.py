from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        CloseToOpen = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        
        for c in s:
            if c in CloseToOpen:
                if stack and CloseToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        
        return True if not stack else False