low=int(input("Enter lower bound:"))
high=int(input("Enter upper bound:"))
count=0
if low%2==0:
    low+=1
while low<high+1:
    count+=1
    low+=2
print(count)