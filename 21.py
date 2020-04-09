# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = None
        merged = None
        while l1 or l2:
            if l1 == None:
                if merged:
                    merged.next = l2
                    l2 = l2.next
                    merged = merged.next
                else:
                    return l2
            elif l2 == None:
                if merged:
                    merged.next = l1
                    l1 = l1.next
                    merged = merged.next
                else:
                    return l1
            elif l1.val < l2.val:
                if merged:
                    merged.next = l1
                    l1 = l1.next
                    merged = merged.next
                else:
                    merged = l1
                    l1 = l1.next
                    start = merged
            else:
                if merged:
                    merged.next = l2
                    l2 = l2.next
                    merged = merged.next
                else:
                    merged = l2
                    l2 = l2.next
                    start = merged
        return start