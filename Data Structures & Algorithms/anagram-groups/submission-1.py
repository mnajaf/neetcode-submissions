class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for x in strs:
            z = "".join(sorted(x))
            if z not in dict:
                dict[z] = []
            dict[z].append(x)

        return list(dict.values())
            
        