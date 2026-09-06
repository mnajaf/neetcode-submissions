class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        l = 0
        r = 0
        length = 0


        while r < len(s):
            if s[r] in sett:
                sett.remove(s[l])
                l+=1
            else:
                sett.add(s[r])
                length = max(length,(r-l) + 1)
                r +=1
        return length
            

            
                

        