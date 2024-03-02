digits=[9,9,9]
flag,i=1,len(digits)-1
while flag!=0 and i>=0:
    if digits[i]!=9:
        digits[i]+=1
        flag=0
    else:
        digits[i]=0
        if i==0:
            digits.insert(0,1)
        i-=1
print(digits)