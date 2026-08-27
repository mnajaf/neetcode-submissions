class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}

        for idx,val in enumerate(nums):
            j = target - val
            if (target - val) in dict:
                return  [dict[target - val],idx]
            
            dict[val] = idx

        