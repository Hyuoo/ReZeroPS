# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=b=0
        o=p=1
        while(l1):
            a += o*l1.val
            o *= 10
            l1 = l1.next
        while(l2):
            a += p*l2.val
            p *= 10
            l2 = l2.next
        a+=b
        ret = ListNode()
        tmp = ret
        while(a):
            tmp.val = a%10
            a//=10
            if(a):
                tmp.next = ListNode()
            tmp = tmp.next
        return ret
