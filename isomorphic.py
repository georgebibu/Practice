s="paper"
t="title"
dict={}
for i in range(len(s)):
    if s[i] in dict and dict[s[i]]!=t[i]:
        print("False")
        break
    elif s[i] not in dict and t[i] in dict.values():
        print("False")
        break
    else:
        dict[s[i]]=t[i]
print("True")