# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head:
            l = []
            while head:
                l.append(head.val)
                head = head.next
            long = len(l) - 1
            idx = 0
            while long > idx:
                if l[idx] != l[long - idx]:
                    return False
                else:
                    idx += 1
        return True