class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        key = []
        
        for s in strs:
            sortedStr = "".join(sorted(s))
            if sortedStr in out:
                out[sortedStr].append(s)
            else:
                out[sortedStr] = [s]

        return list(out.values())

            