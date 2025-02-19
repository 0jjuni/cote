# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        first_bound_start, second_bound_finish = None, None
        rev = None

        if left >= 2:
            for _ in range(left-2):
                cur = cur.next
            first_bound_start = cur
            cur = cur.next
            second_bound_finish = cur
        else:
            first_bound_start = head
            second_bound_finish = head

        for i in range(right-left+1):
            rev, rev.next, cur = cur, rev, cur.next



        if cur:
            second_bound_finish.next = cur

        if left == 1:
            head = rev
        else:
            first_bound_start.next = rev

        return head