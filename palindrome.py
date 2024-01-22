str=input("Enter a string:")
str=str.lower()
rev=""
for i in str:
    if i.isalnum() is False:
        str=str.replace(i,'',1)
    if i.isnumeric():
        str=str.replace(i,'',1)
for i in range(len(str)-1,-1,-1):
    rev=rev+str[i]
if str==rev:
    print(str," is a palindrome")
else:
    print(str," is not a palindrome")