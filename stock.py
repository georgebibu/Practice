n=int(input("Enter number of days:"))
prices=[]
max,left,right=0,0,1
for i in range(n):
    x=int(input(f"Enter price on day {i+1}:"))
    prices.append(x)
while right!=n:
    if prices[left]>=prices[right]:
        left+=1
        right+=1
        continue
    else:
        temp=prices[right]-prices[left]
        right+=1
    if temp>max:
        max=temp
print("Maximum profit:",max)