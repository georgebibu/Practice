# Given an integer array nums, return true if any value appears at least 
# twice in the array, and return false if every element is distinct.
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = set()
        for i in nums:
            if i in l:
                return True
            l.add(i)
        return False
