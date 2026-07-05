# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hs = set()
        while head is not None:
            _tmp = hash(head)
            if _tmp not in hs:
                hs.add(_tmp)
            else:
                return True
            head = head.next
        return False