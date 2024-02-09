s=list(input("Enter string:"))
j=len(s)-1
for i in range(len(s)//2):
    temp=s[j]
    s[j]=s[i]
    s[i]=temp
    j-=1
print(s)
