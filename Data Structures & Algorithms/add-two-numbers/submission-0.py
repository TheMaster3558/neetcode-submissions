# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        sum = head
        carryover = 0
        while l1 is not None:
            added = l1.val + (l2.val if l2 else 0) + carryover
            carryover = 0
            if added >= 10:       
                carryover, added = divmod(added, 10)
            sum.val = added
            l1 = l1.next
            if l2:
                l2 = l2.next
            
            if l1 is not None or l2 is not None:
                sum.next = ListNode()
                sum = sum.next

        while l2 is not None:
            added = l2.val + carryover
            carryover = 0
            if added >= 10:     
                carryover, added = divmod(added, 10)
            sum.val = added
            l2 = l2.next
            if l2 is not None:
                sum.next = ListNode()
                sum = sum.next

        if carryover:
            sum.next = ListNode(carryover)

        return head
        