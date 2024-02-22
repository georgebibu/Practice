n=int(input("Enter number:"))
while n!=1:
    sum=0
    while n>0:
        digit=n%10
        sum+=digit**2
        n=n//10
    n=sum
print(True)