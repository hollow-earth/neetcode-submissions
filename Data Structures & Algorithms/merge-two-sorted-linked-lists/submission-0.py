# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        _tmp = dummy

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                _tmp.next = list1
                list1 = list1.next
            else:
                _tmp.next = list2
                list2 = list2.next
            _tmp = _tmp.next
        
        if list1 is not None:
            _tmp.next = list1
        else:
            _tmp.next = list2


        return dummy.next