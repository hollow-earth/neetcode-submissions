# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        l_ptr, r_ptr = dummy, head

        
        for i in range(n):
            r_ptr = r_ptr.next
        while r_ptr is not None:
            r_ptr = r_ptr.next
            l_ptr = l_ptr.next
        
        l_ptr.next = l_ptr.next.next
        return dummy.next