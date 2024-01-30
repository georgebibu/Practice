stack=[]
flag=0
p=0
s=input("Enter string consisting of parentheses:")
for i in s:
    if i=='(' or i=='[' or i=='{':
        stack.append(i)
        p+=1
    elif i==')':
        if stack[p-1]!='(':
            flag=1
            break
        else:
            del stack[p-1]
            p-=1
    elif i==']':
        if stack[p-1]!='[':
            flag=1
            break
        else:
            del stack[p-1]
            p-=1
    elif i=='}':
        if stack[p-1]!='{':
            flag=1
            break
        else:
            del stack[p-1]
            p-=1
    else:
        flag=1
        break
if len(stack)!=0:
    flag=1
if flag==0:
    print("String is valid")
else:
    print("String is not valid")