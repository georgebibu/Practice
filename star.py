str=list(input("Enter string:"))
leftmost,top,i=[],-1,0
while i<len(str):
    if str[i]!="*":
        leftmost.append(i)
        top+=1
        i+=1
    else:
        del str[i]
        if top!=-1:
            del str[leftmost[top]]
            top-=1
            leftmost.pop()
            i-=1
str="".join(str)
print(str)