def encode(strs: list[str]) -> str:
    res=""
    for i in strs:
        if i=="":
            res+="$.$"
        res+=i
        res+="%.%"
    res=res[:-1]
    res=res[:-1]
    res=res[:-1]
    return res
def decode(s: str) -> list[str]:
    strs=[]
    s=list(s)
    n=len(s)
    temp=""
    i=0
    while i<n:
        if s[i]=="%" and i<n-2:
            if s[i+1]=="." and s[i+2]=="%":
                if temp=="":
                    i+=3
                    continue
                strs.append(temp)
                temp=""
                i+=3
                continue
        if s[i]=="$" and i<n-2:
            if s[i+1]=="." and s[i+2]=="$":
                strs.append("")
                temp=""
                i+=3
                continue
        temp+=s[i]
        i+=1
    if temp!="":
        strs.append(temp)
    return strs
input=["","   ","!@#$%^&*()_+","LongStringWithNoSpaces","Another, String With, Commas"]
cipher=encode(input)
print(f"Cipher:{cipher}\n")
plain=decode(cipher)
print(f"Plain:{plain}")