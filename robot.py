instructions=list(input("Enter intsructions:"))
pos,dir,d,flag=[0,0],['N','E','S','W'],0,0
for i in instructions:
    if i=='G':
        if dir[d]=='N':
            pos[1]+=1
        elif dir[d]=='S':
            pos[1]-=1
        elif dir[d]=='W':
            pos[0]-=1
        else:
            pos[0]+=1
    elif i=='R':
        d=(d+1)%4
    elif i=='L':
        if d==0:
            d=3
        else:
            d-=1
    else:
        print("Invalid instruction")
if pos==[0,0] or d!=0:
    print(True)
else:
    print(False)