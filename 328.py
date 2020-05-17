# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if head.next:
            even = ListNode(head.next.val)
        else:
            return head
        parity = 1
        def addEm(cur, other, ll):
            nonlocal parity, even
            node = ListNode(ll.val)
            cur.next = node
            cur = cur.next
            parity *= -1
            if ll.next:
                addEm(other, cur, ll.next)
            elif parity < 0:
                cur.next = even
            else:
                other.next = even
        if head.next.next:
            addEm(head, even, head.next.next)
        return head