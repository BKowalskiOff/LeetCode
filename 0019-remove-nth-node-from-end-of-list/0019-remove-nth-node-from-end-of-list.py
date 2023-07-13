# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        to_remove_prev = None
        curr = head
        i = 1
        while curr:
            if i == n + 1:
                to_remove_prev = head
                curr = curr.next
                i += 1
                continue
            if to_remove_prev:
                to_remove_prev = to_remove_prev.next
            curr = curr.next
            i += 1

        if to_remove_prev:
            if to_remove_prev == head:
                head.next = head.next.next
                return head
            if to_remove_prev.next:
                to_remove_prev.next = to_remove_prev.next.next
            return head
        
        return head.next