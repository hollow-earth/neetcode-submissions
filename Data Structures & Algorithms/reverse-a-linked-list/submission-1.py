# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            prev, nxt = None, None # Setup
            curr = head
            while curr is not None:
                # 0. Set prev, nxt
                # 1. Find nxt, store aside for now
                # 2. Take curr, make it point to prev
                # 3. Then move prev to curr, and curr to next
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev