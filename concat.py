n=int(input("Enter length of array:"))
nums=[]
ans=[]
for i in range(n):
    x=int(input("Enter element:"))
    nums.append(x)
    ans.append(x)
for i in nums:
    ans.append(i)
print(ans)
