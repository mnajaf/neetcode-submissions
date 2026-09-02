class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        counter = 0

        for i in range(len(nums) - 1,-1,-1):
            if nums[i] == 1:
                counter += 1
            else:
                counter = 0
            maxx = max(maxx,counter)
            nums.pop()
        return maxx
            
            


            

