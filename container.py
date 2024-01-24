n=int(input("Enter length:"))
height=[]
a=0
for i in range(n):
    x=int(input("Enter height:"))
    height.append(x)
for i in range(n):
    for j in range(i+1,n):
        if height[i]<height[j]:
            temp=height[i]*(j-i)
        else:
            temp=height[j]*(j-i)
        if temp>a:
            a=temp
print(f"Maximum area is:{a}")