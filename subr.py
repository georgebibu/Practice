s=input("Enter string:")
s=s.upper()
s=list(s)
c=[]
max=0
k=int(input("Enter number of replacements:"))
for i in range(k):
    x=int(input("Enter index of letter to be replaced:"))
    q=input("Enter letter:")
    q=q.upper()
    s[x]=q
for i in s:
    if i not in c:
        c.append(i)
for p in c:
    count=0
    for i in s:
        if i==p:
            count+=1
        else:
            count=0
            continue
        if count>max:
            max=count
print(max)