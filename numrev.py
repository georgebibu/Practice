x=int(input("Enter number:"))
temp,rev=x,0
if x<0:
    print(False)
else:
    while x>0:
        d=x%10
        rev=(rev*10)+d
        x//=10
    if temp==rev:
        print(True)
    else:
        print(False)