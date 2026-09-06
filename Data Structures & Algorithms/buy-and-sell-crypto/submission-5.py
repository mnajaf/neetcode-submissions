class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        res = 0
        

        print(prices)
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                res = max(res,(prices[r] - prices[l]))
                r += 1
        return res
            


        