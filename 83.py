# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        start = ListNode(head.val)
        starthere = start
        while head.next:
            if head.val == head.next.val:
                head = head.next
            else:
                start.next = ListNode(head.next.val)
                start = start.next
                head = head.next
        return starthere