#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
flag=0
nums=[]
n=int(input("Enter length of list:"))
for i in range(n):
    x=int(input("Enter element:"))
    nums.append(x)
t=int(input("Enter target:"))
for i in range(n):
    for j in range(i+1,n):
        if nums[i]+nums[j]==t:
            flag=1
            print(f"Elements at indices {i} and {j} add upto {t}")
            break
    if flag==1:
        break
if flag==0:
    print("No pair of elements in the list adds upto the target")
