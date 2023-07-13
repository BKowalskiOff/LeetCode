# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_head = ListNode()
        merged = merged_head
        while list1 and list2:
            merged.next = ListNode()
            merged = merged.next
            if list1.val > list2.val:
                merged.val = list2.val
                list2 = list2.next
                continue
            merged.val = list1.val
            list1 = list1.next
        
        while list1:
            merged.next = ListNode()
            merged = merged.next
            merged.val = list1.val
            list1 = list1.next

        while list2:
            merged.next = ListNode()
            merged = merged.next
            merged.val = list2.val
            list2 = list2.next
        
        merged.next = None
        merged_head = merged_head.next

        return merged_head