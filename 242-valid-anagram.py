class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        check, check2 = {}, {}

        for i in s:
            if i in check:
                check[i] += 1
            else:
                check[i] = 1

        for j in t:
            if j in check2:
                check2[j] += 1
            else:
                check2[j] = 1

        for k in check:
            if k in check and k in check2:
                if check[k] == check2[k]:
                    continue
                else:
                    return False
            else:
                return False
        return True