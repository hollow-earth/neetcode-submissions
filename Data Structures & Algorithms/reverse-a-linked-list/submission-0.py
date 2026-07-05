# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: # length is 0 or 1
            return head
        else:
            prev = None
            curr = head
            nxt = None
            while curr is not None:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev



