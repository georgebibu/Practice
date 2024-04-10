people=[3,5,3,4]
limit=5
right=len(people)-1
if right==0:
    print(1)
    exit()
count,left=0,0
people.sort()
current=people[left]+people[right]
while left<right:
    if people[right]==limit:
        right-=1
        count+=1
        current=people[left]+people[right]
    elif people[left]==limit:
        left+=1
        count+=1
        current=people[left]+people[right]
    elif current<limit:
        left+=1
        right-=1
        count+=1
        current=people[left]+people[right]
    elif current>limit:
        right-=1
        current=people[left]+people[right]
        count+=1
    else:
        left+=1
        right-=1
        count+=1
        current=people[left]+people[right]
if left==right:
    count+=1
print(count)