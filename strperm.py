s1="dca"
s2="dcda"
s1=list(s1)
original=s1.copy()
s2=list(s2)
n=len(s2)
window=len(s1)
start,end=0,window
while end<=n:
    for i in range(start,end):
        if s2[i] in s1:
            print(s1)
            s1.remove(s2[i])
            if s1==[]:
                print("True")
                exit()
        else:
            s1=original.copy()
            start+=1
            end+=1
            break
print("False")