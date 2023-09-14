from typing import List
from collections import defaultdict
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
    
    def moreEfficientGroupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        # create a hash map to store the groups of anagrams
        hashMap = defaultdict(list)

        for s in strs:
            # sort the string and use it as a key to identify the group
            key = "".join(sorted(s))
            # append the string to the appropriate group
            hashMap[key].append(s)
        
        # convert the hash map values (which are lists of strings) to a list of lists of strings
        return list(hashMap.values())