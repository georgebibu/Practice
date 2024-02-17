n=int(input("Enter column number"))
s=""
a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
while n!=0:
    s+=a[int((n-1)%26)]
    n=(n-1)//26
print("".join(reversed(s)))