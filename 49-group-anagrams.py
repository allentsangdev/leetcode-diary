from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create a hash map to determine which group should a string belongs to
        hashMap = {}
        groupNumber = 1
        for i in strs:
            key = "".join(sorted(i))
            if i not in hashMap:
                hashMap[key] = groupNumber
                groupNumber += 1
        
        result = []
        for i in range(groupNumber+1):
            result.append([])
        for i in strs:
            key = "".join(sorted(i))
            result[hashMap[key]].append(i)
        return result