customers=list(map(str,input("Enter list:").split()))
hour,l,r=0,0,0
if customers[0]=='Y':
    prev='Y'
else:
    prev='N'
for i in range(len(customers)):
    if customers[i]=='Y':
        r+=1
min=l+r
for i in range(1,len(customers)):
    if prev=='Y':
        r-=1
    else:
        l+=1
    if l+r<min:
        hour=i
        min=l+r
    prev=customers[i]
if prev=='Y':
    r-=1
else:
    l+=1
if l+r<min:
    hour=i+1
print(hour)