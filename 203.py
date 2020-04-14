# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        start = None
        while head:
            if val == head.val:
                head = head.next
            else:
                start = head
                break
        if head:
            while head.next:
                if val != head.next.val:
                    head = head.next
                else:
                    head.next = head.next.next
        return start