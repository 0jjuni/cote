# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current:
            nxt = current.next
            if not nxt:
                break
            current.val, nxt.val = nxt.val, current.val
            current = nxt.next
        return head