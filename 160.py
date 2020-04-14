# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodesA = []
        while headA:
            nodesA.append(headA)
            headA = headA.next
        nodesB = []
        while headB:
            nodesB.append(headB)
            headB = headB.next
        last = None
        while nodesA and nodesB:
            a = nodesA.pop()
            b = nodesB.pop()
            if a != b:
                break
            else:
                last = a
        return last