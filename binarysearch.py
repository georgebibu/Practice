#You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
#Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.
#Your solution must run in O(logn) time.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high=len(nums)-1
        low=0
        mid=(low+high)//2
        while(low<=high):
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                low=mid+1
                mid=(low+high)//2
            else:
                high=mid-1
                mid=(low+high)//2
        return -1
        
