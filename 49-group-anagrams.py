from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create a hash map to determine which group should a string belongs to
        hashMap = {}
        groupNumber = 1
        for i in strs:
            key = str(sorted(i))
            if i not in hashMap:
                hashMap[i] = groupNumber
                groupNumber += 1
        
        result = []
        for i in range(groupNumber+1):
            result.append([])
        for i in strs:
            result[hashMap[str(sorted(i))]].append(i)
        return result