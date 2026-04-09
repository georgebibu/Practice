#Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            temp = [0]*26
            for j in i:
                temp[ord(j) - ord("a")] += 1
            res[tuple(temp)].append(i)
        return list(res.values())
