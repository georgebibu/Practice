s=input("Enter string:")
t=input("Enter subsequence:")
j=0
for i in s:
    if t[j]==i:
        j+=1
if j!=len(t):
    print("Not a subsequence")
else:
    print("Is a subsequence")