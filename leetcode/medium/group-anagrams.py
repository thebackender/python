#https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs):
        if strs == [""]:
            return [[""]]
        if len(strs) == 1:
            return [strs]
        data = {}
        for a in strs:
            i = str(sorted(a))
            if i not in data:
                data[i] = []
        for s in strs:
            j = str(sorted(s))
            data[j].append(s)
        arr = []
        for k,v in data.items():
            arr.append(v)
        return arr
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))