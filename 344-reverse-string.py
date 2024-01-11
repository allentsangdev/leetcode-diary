from typing import List

class Solution1:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)-1,-1,-1):
            s.append(s.pop(i))

# with 2 pointer
# Time: O(n) Space: O(1)
class Solution2:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L, R = 0, len(s)-1

        while L < R:
            s[L], s[R] = s[R], s[L]
            L+=1 
            R-=1

# with a stack
# Time: O(n) Space: O(n)
class Solution3:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []

        for i in range(len(s)-1,-1,-1):
            stack.append(s[i])
        
        for i in range(len(s)):
            s[i] = stack[i]

# with recursion
# Time: O(n) Space: O(n)
class Solution3:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(L,R):
            if L < R:
                s[L], s[R] = s[R], s[L]
                reverse(L+1, R-1)
        
        reverse(0, len(s)-1)