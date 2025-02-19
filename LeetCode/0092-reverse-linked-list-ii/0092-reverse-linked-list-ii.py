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

        if left == 1: # 처음부터 역순 시작할 때
            left_before = head
            rev_finish = head            
        else:
            for _ in range(left-2): # 역순되지 않는 값들의 마지막값을 저장하기 위해 -2만큼 반복
                cur = cur.next
            left_before = cur # 역순되지 않은 값들 중 마지막 값
            cur = cur.next
            rev_finish = cur # 역순될 값들 중 마지막에 올 값

        for i in range(right-left+1): # 역순
            rev, rev.next, cur = cur, rev, cur.next

        if cur: # right뒤쪽에 남은게 있다면 rev 뒤에 추가
            rev_finish.next = cur

        if left == 1: # 처음부터 시작했으므로 rev를 return
            head = rev
        else:
            left_before.next = rev

        return head