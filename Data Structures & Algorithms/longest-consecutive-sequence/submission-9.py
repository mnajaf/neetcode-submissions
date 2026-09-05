class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        a = set()
        maxx = 0

        for num in nums:
            a.add(num)

        

        for num in a:
            counter = 1
            if (num - 1) not in a:
                while (num + 1) in a:
                    counter += 1
                    num = num + 1
            
            maxx = max(maxx,counter)
        return maxx

        