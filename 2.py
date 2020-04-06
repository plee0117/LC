# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = delist(l1)
        n2 = delist(l2)
        su = n1 + n2
        return relist(su)
        
def delist(l):
    n = 0
    i=0
    while l:
        n += l.val* 10**i
        if l.next == None:
            break
        else:
            l = l.next
            i += 1
    return n


def relist(n):
    nass = str(n)
    l = ListNode(nass[0])
    i = 1
    end = len(nass)
    while i < end:
        rem = l
        l = ListNode(nass[i])
        l.next = rem
        i += 1
    return(l)
