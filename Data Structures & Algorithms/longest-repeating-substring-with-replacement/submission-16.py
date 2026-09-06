class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0

        n = len(s)
        maxFreq = 0
        count = {}
        length = 0



        for r in range(n):
            
            if s[r] not in count:
                count[s[r]] = 0
            count[s[r]] += 1

            maxFreq = max(maxFreq,count[s[r]])

            while ((r-l) + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            
            length = max(length,(r-l) + 1)
        return length




        