flowerbed=[1,0,0,0,1]
n=2
if n==0:
    print("True")
l=len(flowerbed)
if l==1:
    if flowerbed[0]==0:
        print("True")
    else:
            print("False")
if l==2:
    if flowerbed[0]==1 or flowerbed[1]==1:
        print("False")
    else:
        if n<=1:
            print("True")
        else:
            print("False")
if flowerbed[0]==0 and flowerbed[1]==0:
    n-=1
    flowerbed[0]=1
if flowerbed[l-1]==0 and flowerbed[l-2]==0:
    n-=1
    flowerbed[l-1]=1
for i in range(1,l-2):
    if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0:
        flowerbed[i]=1
        n-=1
if n<=0:
    print("True")
else:
    print("False")