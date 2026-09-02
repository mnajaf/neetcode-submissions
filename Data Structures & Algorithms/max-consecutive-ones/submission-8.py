class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        counter = 0

        for num in nums:
            if num == 1:
                counter += 1
            else:
                counter = 0
            maxx = max(maxx,counter)
        return maxx
            
            


            

