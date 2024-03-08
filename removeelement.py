nums=list(map(int,input("Enter nums:").split()))
val=int(input("Enter val:"))
i,k=0,0
while i<len(nums):
    if nums[i]==val:
        nums.pop(i)
    else:
        k+=1
        i+=1
print(nums)