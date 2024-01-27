s=input("Enter string:")
c=[]
for i in s:
    if i not in c:
        c.append(i)
list=[]
str=""
out=""
max=len(c)
i=0
while i+max-1<len(s):
    for j in range(0,max):
        if s[i+j] not in list:
            list.append(s[i+j])
            str+=(s[i+j])
        else:
            break
    if len(str)>len(out):
        out=str
    i=i+1
    list.clear()
    str=""
print("Longest substring without repeating characters:",out)
print("Length of substring:",len(out))