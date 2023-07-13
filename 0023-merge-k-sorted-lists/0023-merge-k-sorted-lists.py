# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        has_next = False
        
        merged_head = None
        merged = None

        while True:
            has_next = False
            min = 10e4
            min_index = -1
            number_of_not_none = 0
            for i, l in enumerate(lists):
                if l == None:
                    continue
                number_of_not_none += 1
                if not l.next == None:
                    has_next = True
                if  l.val <= min:
                    min_index = i
                    min = l.val

            if number_of_not_none > 1:
                has_next = True

            if min_index == -1:
                break
            if merged == None:
                merged = ListNode(-10e4-1)

            merged.val = min
            if merged_head == None:
                merged_head = merged
           
            if has_next:
                merged.next = ListNode()
                merged = merged.next
    
            lists[min_index] = lists[min_index].next
            if lists[min_index] == None:
                lists = lists[:min_index] + lists[min_index + 1:]
    
        return merged_head
            