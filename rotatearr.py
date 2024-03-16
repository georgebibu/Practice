nums=[1,2,3,4,5,6,7]
k=3
temp=[]
for i in nums:
    temp.append(0)
start=0
while start<len(nums):
    temp[(start+k)%len(nums)]=nums[start]
    start+=1
nums=temp
print(nums)