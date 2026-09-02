class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0

        for idx,num in enumerate(nums):
            if num != val:
                nums[k] = num
                k += 1
        return k

        