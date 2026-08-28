class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        z = {}

        for num in nums:
            if num not in z:
                z[num] = 0
            
            z[num] += 1

        sorted_nums = sorted(z, key = z.get,reverse = True)

        return sorted_nums[:k]
        

        