from typing import List

class Solution:    
    def evalRPN(self, tokens: List[str]) -> int:
        operatorMap = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
        }

        stack = []

        for i in tokens:
            if i not in operatorMap:
                stack.append(int(i))
            elif i in operatorMap:
                x = stack.pop()
                y = stack.pop()
                stack.append(int(operatorMap[i](y,x)))
        return stack[0]