#Given an integer array nums and an integer k, return the k most frequent elements within the array.
#The test cases are generated such that the answer is always unique.
#You may return the output in any order.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}
        res = {}
        length = len(nums)
        for i in range(length):
            x[nums[i]] = 1 + x.get(nums[i], 0)
            res[i + 1] = []
        for i in x:
            freq = x[i]
            res[freq].append(i)
        print(res)
        result = []
        i = length
        while k > 0 and i > 0:
            for j in res[i]:
                result.append(j)
                k -= 1
            i -= 1
        return result
