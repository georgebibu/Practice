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
        
