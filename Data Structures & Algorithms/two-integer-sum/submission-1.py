class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}

        for idx,val in enumerate(nums):
            j = target - val
            if j in dict:
                return  [dict[j],idx]
            
            dict[val] = idx

        