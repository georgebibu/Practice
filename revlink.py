class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
ptr,head,tail,after,before=None,None,None,None,None
n=int(input("Enter length of list:"))
for i in range(n):
    data=int(input("Enter data:"))
    p=Node(data)
    if head==None:
        head,tail=p,p
    else:
        tail.next=p
        tail=p
ptr=head
tail=head
after=ptr.next
while ptr!=None:
    ptr.next=before
    before=ptr
    head=ptr
    ptr=after
    if after==None:
        break
    after=after.next
ptr=head
while ptr!=None:
    print(ptr.data)
    ptr=ptr.next