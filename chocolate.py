prices,money=[3,2,3],3
prices.sort()
count=0
original=money
for i in prices:
    if i<=money:
        money-=i
        count+=1
    else:
        print(original)
        break
    if count==2:
        print(money)
        break