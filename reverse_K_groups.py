#You are given the head of a singly linked list head and a positive integer k.
#You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on.
#If there are fewer than k nodes left, leave the nodes as they are.
#Return the modified list after reversing the nodes in each group of k.
#You are only allowed to modify the nodes' next pointers, not the values of the nodes.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            kth = self.getKth(group_prev, k)
            if not kth:
                break
            group_next = kth.next
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
        return dummy.next


    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
