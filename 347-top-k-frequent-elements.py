from typing import List
from collections import defaultdict

class Solution:    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Create the hash map to store the frequency of each number
        hashMap = {}
        for i in nums:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1

        # Step 2: Create a reverse hash map with frequencies as keys and numbers as values
        reverseHashMap = defaultdict(list)
        for key, value in hashMap.items():
            reverseHashMap[value].append(key)

        # Step 3: Create the result list with the top k frequent numbers
        unique_frequencies = sorted(reverseHashMap.keys(), reverse=True)
        result = []
        for freq in unique_frequencies:
            for num in reverseHashMap[freq]:
                if len(result) < k:
                    result.append(num)
                else:
                    break
            if len(result) >= k:
                break

        return result

testNumber = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
top = 10

solution = Solution()
print(solution.topKFrequent2(testNumber, top))