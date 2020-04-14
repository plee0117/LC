# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head:
            new = ListNode(head.val)
            while head.next:
                temp = new
                head = head.next
                new = ListNode(head.val)
                new.next = temp
            return new
        else:
            return None