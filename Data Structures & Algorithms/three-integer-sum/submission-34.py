class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)


        for idx,val in enumerate(nums):
            left = idx + 1
            right = len(nums) - 1
            if idx > 0 and val == nums[idx - 1]:
                continue
            while left < right:
                if val + nums[left] + nums[right] < 0:
                    left += 1
                elif val + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                        result.append([nums[idx],nums[left],nums[right]])

                        left += 1
                            
                        while left < right and nums[left] == nums[left - 1]:
                            left +=1
                        right -= 1
        
        return result



