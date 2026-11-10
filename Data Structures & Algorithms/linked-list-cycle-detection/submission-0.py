# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        left = head
        right = head.next

        if not right or not right.next:
            return False

        while right and left != right:
            left = left.next
            right = right.next
            if not right:
                return False
            right = right.next
        if right:
            return True
        return False
        
        