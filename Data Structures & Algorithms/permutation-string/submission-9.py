class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 

        count = {}
        length = len(s1)
        if len(s1) > len(s2):
            return False

        for char in s1:
            if char not in count:
                count[char] = 0
            count[char] += 1
        
        l = 0

        for r in range(len(s2)):
            if s2[r] in count:
                count[s2[r]] -= 1

            if ((r-l) + 1) == length:

                if all(x==0 for x in count.values()):
                    return True

                if s2[l] in count:
                    count[s2[l]] += 1
                l += 1
        return False
            

            

        