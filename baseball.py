n=int(input("Enter length of list:"))
digits=["-9","-8","-7","-6","-5","-4","-3","-2","-1","0","9","8","7","6","5","4","3","2","1"]
list=[]
sum=0
record=[]
for i in range(n):
    x=input("Enter element:")
    list.append(x)
for i in list:
    if i in digits:
        i=int(i)
        sum+=i
        record.append(i)
    else:
        if i=="C":
            sum-=record[len(record)-1]
            record.pop()
        elif i=="D":
            record.append(2*record[len(record)-1])
            sum+=record[len(record)-1]
        elif i=="+":
            if len(record)>=2:
                record.append(record[len(record)-1]+record[len(record)-2])
                sum+=record[len(record)-1]
            else:
                print("Error")
                break
        else:
            print("Error")
            break
    print(record)
print(sum)
