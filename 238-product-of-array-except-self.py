from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        prefix = []
        suffix = []
        
        count = 1
        for i in nums:
            prefix.append(i * count)
            count = i * count

        count = 1
        for i in range(len(nums)-1, -1 , -1):
            suffix.append(nums[i] * count)
            count = nums[i] * count

        suffix.reverse()

        for i in range(len(nums)):    
            if i - 1 == -1:
                answer.append(suffix[i+1])
            elif i + 1 == len(nums):
                answer.append(prefix[i-1])
            else:
                answer.append(prefix[i-1] * suffix[i + 1])
        
        print(prefix,suffix)
        return answer

    from typing import List

class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        postfix = []

        # fill in the prefix list
        pre = 1
        for i in range(len(nums)):
            pre *= nums[i]
            prefix.append(pre)
            
        # fill in the postfix list
        post = 1
        for i in range(len(nums)-1, -1, -1):
            postfix.append(post * nums[i])
            post *= nums[i]
        postfix.reverse()
                    
        for i in range(len(nums)):
            if i == 0:
                res.append(postfix[i+1])
            elif i == len(nums)-1:
                res.append(prefix[i-1])
            else:
                res.append(prefix[i-1] * postfix[i+1])
        return res

    
# Testing
numberList = [1,2,3,4]

soultion = Solution()
print(soultion.productExceptSelf(numberList))


