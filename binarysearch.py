nums=[-1,0,2,4,6,8]
target=0
high=len(nums)-1
low=0
mid=(low+high)//2
while(low<=high):
    if nums[mid]==target:
        print(f"Found at {mid}")
        exit()
    elif target>nums[mid]:
        low=mid+1
        mid=(low+high)//2
    else:
        high=mid-1
        mid=(low+high)//2
print("Not found")