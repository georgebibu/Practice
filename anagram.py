#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
l=[]
flag=0
str1=input("Enter string:")
str=str1
str2=input("Enter anagram:")
if len(str1)!=len(str2):
    print("Not a valid anagram")
    flag=1
else:
    for i in str2:
        if i in str1:
            str1=str1.replace(i,'',1)
        else:
            print("Not a valid anagram")
            flag=1
            break
if flag==0:
    print(str2+" is a valid anagram of "+str)
    

