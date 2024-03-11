nums1=set(list(map(int,input("Enter nums1:").split())))
nums2=set(list(map(int,input("Enter nums2:").split())))
answer=[[],[]]
for i in nums1:
    if i not in nums2 and i not in answer[0]:
        answer[0].append(i)
for i in nums2:
    if i not in nums1 and i not in answer[1]:
        answer[1].append(i)
print(answer)