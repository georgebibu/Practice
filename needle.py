haystack=input("Enter string:")
needle=input("Enter substring to be searched:")
i=0
while i+len(needle)-1<len(haystack):
    p,flag=0,0
    for j in range(i,i+len(needle)):
        if haystack[j]!=needle[p]:
            flag=1
            break
        p+=1
    if flag==0:
        break
    i+=1
print("First occurence of ",needle," in ",haystack," is:",i)