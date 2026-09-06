class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        maxx = 0
        res = 0

        while left < right:
            ans = min(heights[left],heights[right]) * (right-left)
            res = max(res,ans)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return res
            

        