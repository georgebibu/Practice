s=input("Enter sentence:")
l,i,flag=0,len(s)-1,0
while i>=0 and s[i]!=' ' or flag==0:
    if s[i]!=' ':
        flag=1
    if flag==1:
        l+=1
    i-=1
print("Length:",l)