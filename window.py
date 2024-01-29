s=list(input("Enter string:"))
t=input(("Enter substring:"))
out=""
c={}
window={}
wc=0
start,end,i,j=0,0,0,0
for x in t:
    if x not in c:
        c[x]=1
        window[x]=0
    else:
        c[x]+=1
while(i!=len(s)):
    if wc!=len(c) and j<len(s):
        if s[j] in t:
            window[s[j]]+=1
            if window[s[j]]==c[s[j]]:
                wc+=1
        j+=1 
    elif wc==len(c):
        if start-end==0 or j-i<end-start:
            start=i
            end=j
        if s[i] in t:
            if window[s[i]]==c[s[i]]:
                wc-=1
            window[s[i]]-=1
        i+=1
    else:
        i+=1
while start<end:
    out=out+s[start]
    start+=1
print(out)