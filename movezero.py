nums=[0,1,0,3,12]
end=len(nums)-1
i=0
while i<end:
    if nums[i]==0:
        nums.pop(i)
        nums.append(0)
        end-=1
    else:
        i+=1