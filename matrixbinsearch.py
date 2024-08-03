matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=10
for nums in matrix:
    high=len(nums)-1
    low=0
    mid=(low+high)//2
    while(low<=high):
        if nums[mid]==target:
            print(f"Found at {mid} in {nums}")
            exit(0)
        elif target>nums[mid]:
            low=mid+1
            mid=(low+high)//2
        else:
            high=mid-1
            mid=(low+high)//2
print("Not found")