nums = [1,2,1,0,1]
n=len(nums)
if n==1:
    print(True)
    exit()
def jump(nums,index):
    if index==n-1:
        return True
    if nums[index]==0:
        return False
    distance=nums[index]
    if distance>n-1:
        distance=n-1
    while(distance>=1):
        if jump(nums,index+distance) is False:
            distance-=1
        else:
            return True
    return False
print(jump(nums,0))