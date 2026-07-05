# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(next=head)
        fast = head
        slow = dummy

        while fast is not None and fast.next is not None and slow is not None:
            if fast == slow:
                return True
            else:
                fast = fast.next.next
                slow = slow.next
        return False