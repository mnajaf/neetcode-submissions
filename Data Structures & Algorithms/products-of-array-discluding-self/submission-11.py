class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)


        for idx in range(1,len(nums)):
            prefix[idx] = prefix[idx - 1] * nums[idx - 1]

        
        for idx in range(len(nums) -2, -1, -1):
            postfix[idx] = postfix[idx + 1] * nums[idx + 1]
        
        
        for i in range(len(nums)):
            postfix[i] = postfix[i] * prefix[i]

        return postfix
            






