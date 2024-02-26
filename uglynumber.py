def isprime(n):
    if n==1:
        return False
    for j in range(2,n//2+1):
        if n%j==0:
            return False
    return True
n=int(input("Enter number:"))
flag,set=0,[2,3,5]
for i in range(2,n+1):
    if n%i==0 and ((isprime(i) and i not in set) or (isprime(n//i) and n//i not in set)) and (i!=1 or n//i!=1):
        print("Number is not ugly")
        flag=1
        break
if flag==0:
    print("Number is ugly")