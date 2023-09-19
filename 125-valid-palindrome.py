from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove all non-alphanumeric characters
        
        phrase = []
        for i in s:
            if i.isalnum():
                phrase.append(i.lower())
        
        print(phrase)
        first, last = 0, len(phrase) - 1

        for i in range(len(phrase)):
            if phrase[first] != phrase[last]: 
                return False
            else:
                first += 1
                last -= 1
        return True

s = "A man, a plan, a canal: Panama"
solution = Solution()
x = solution.isPalindrome(s)
print(x)

