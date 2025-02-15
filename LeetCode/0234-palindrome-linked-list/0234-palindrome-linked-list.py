# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q = []
        node = head
        while node:
            q.append(node.val)
            node = node.next
        return q == q[::-1]