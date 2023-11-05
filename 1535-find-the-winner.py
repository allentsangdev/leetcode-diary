from typing import List

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[0],arr[1])
        if k >= len(arr):
            return max(arr)
        count = 0
        while count != k:
            if (arr[0] > arr[1]):
                count += 1
                arr.append(arr.pop(1))
            else:
                count = 1
                arr.append(arr.pop(0))
        return arr[0]

num = [2,1,3,5,4,6,7]        
solution = Solution()

solution.getWinner(num,2)