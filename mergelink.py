class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=int(input("Enter length of list 1:"))
list1,list2,tail1,tail2=None,None,None,None
for i in range(n1):
    data=int(input("Enter data:"))
    new_node=Node(data)
    new_node.next=None
    if(list1==None):
        list1=new_node
        tail1=new_node
    else:
        tail1.next=new_node
        tail1=new_node
n2=int(input("Enter length of list 2:"))
for i in range(n2):
    data=int(input("Enter data:"))
    new_node=Node(data)
    new_node.next=None
    if(list2==None):
        list2=new_node
        tail2=new_node
    else:
        tail2.next=new_node
        tail2=new_node
head=None
tail=None
p1=list1
p2=list2
while(p1!=None and p2!=None):
    if(p1.data<p2.data):
        new_node=Node(p1.data)
        if(head==None):
            head=new_node
            tail=new_node
        else:
            tail.next=new_node
            tail=new_node
        p1=p1.next
    elif(p2.data<p1.data):
        new_node=Node(p2.data)
        if(head==None):
            head=new_node
            tail=new_node
        else:
            tail.next=new_node
            tail=new_node
        p2=p2.next
    else:
        new_node=Node(p1.data)
        if(head==None):
            head=new_node
            tail=new_node
        else:
            tail.next=new_node
            tail=new_node
        new_node=Node(p2.data)
        if(head==None):
            head=new_node
            tail=new_node
        else:
            tail.next=new_node
            tail=new_node
        p1=p1.next
        p2=p2.next
if(p1!=None):
    while(p1!=None):
        new_node=Node(p1.data)
        if(head==None):
            head=new_node
            tail=new_node
        else:
            tail.next=new_node
            tail=new_node
        p1=p1.next
else:
    while(p2!=None):
        new_node=Node(p2.data)
        if(head==None):
            head=new_node
            tail=new_node
        else:
            tail.next=new_node
            tail=new_node
        p2=p2.next
while(head!=None):
    print(head.data,end=" ")
    head=head.next