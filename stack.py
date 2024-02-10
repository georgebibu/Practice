op=""
s_top=-1
m_top=-1
stack=[]
min=[]
stack
while True:
    op=input("Enter operation:")
    if op=="push":
        x=int(input("Enter number:"))
        if s_top==-1:
            min.append(x)
            m_top+=1
        else:
            if x<min[m_top]:
                min.append(x)
                m_top+=1
            else:
                min.append(min[m_top])
                m_top+=1
        stack.append(x)
        s_top+=1
    elif op=="pop":
        if s_top==-1:
            print("Empty")
        else:
            stack.pop()
            s_top-=1
            min.pop()
            m_top-=1
    elif op=="getMin":
        if m_top==-1:
            print("Empty")
        else:
            print("Minimum:",min[m_top])
    elif op=="top":
        if m_top==-1:
            print("Empty")
        else:
            print("Top:",stack[s_top])
    elif op=="exit":
        break
    else:
        print("Error")