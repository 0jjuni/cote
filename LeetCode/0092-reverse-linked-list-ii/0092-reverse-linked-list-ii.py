# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        left_before, rev_finish= None, None
        rev = None

        if left >= 2:
            for _ in range(left-2):
                cur = cur.next
            left_before = cur
            cur = cur.next
            rev_finish = cur
        else:
            left_before = head
            rev_finish = head

        for i in range(right-left+1):
            rev, rev.next, cur = cur, rev, cur.next

        if cur:
            rev_finish.next = cur


        if left == 1:
            head = rev
        else:
            left_before.next = rev

        return head