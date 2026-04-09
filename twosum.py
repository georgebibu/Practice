#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = {}
        for i in range(len(nums)):
            if target - nums[i] in k:
                return [k[target - nums[i]], i]
            k[nums[i]] = i
