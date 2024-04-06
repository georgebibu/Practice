nums=[1,0,1,1]
k=1
l=len(nums)
if l==1:
    print(True)
    exit
list=[]
if k>=l-1:
    for i in nums:
        if i in list:
            print(True)
            exit()
        list.append(i)
    print(False)
    exit()
list=[]
for i in range(k+1):
    if nums[i] in list:
        print(True)
        exit()
    list.append(nums[i])
for i in range(k+1,l):
    list.pop(0)
    if nums[i] in list:
        print(True)
        exit()
    list.append(nums[i])
print(False)