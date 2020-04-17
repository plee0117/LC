# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        if head:
            original = head
            rev = ListNode(head.val)
            while head.next:
                temp = rev
                head = head.next
                rev = ListNode(head.val)
                rev.next = temp
            while original:
                if original.val == rev.val:
                    original = original.next
                    rev = rev.next
                else:
                    return False
        return True