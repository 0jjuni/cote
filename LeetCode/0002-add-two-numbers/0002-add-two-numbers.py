class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        is_over = 0

        while l1 or l2 or is_over:
            sum_value = is_over
            if l1:
                sum_value += l1.val
                l1 = l1.next
            if l2:
                sum_value += l2.val
                l2 = l2.next

            temp.next = ListNode(sum_value % 10)
            temp = temp.next
            
            is_over = sum_value // 10
        return dummy.next
            