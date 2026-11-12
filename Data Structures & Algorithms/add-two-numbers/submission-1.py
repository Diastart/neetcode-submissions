# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        head = node
        remainder = 0
        while l1 or l2 or remainder:
            if l1 and l2:
                temp = l1.val + l2.val
            elif l1:
                temp = l1.val
            elif l2:
                temp = l2.val
            else:
                temp = 0
            temp += remainder
            node.val = temp % 10
            remainder = 1 if temp >= 10 else 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if not l1 and not l2 and not remainder:
                return head
            node.next = ListNode()
            node = node.next
        return head
            
            
            

        

        