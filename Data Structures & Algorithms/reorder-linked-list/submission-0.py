# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        len = 0
        h = head
        while h:
            len += 1
            h = h.next

        stack = []
        
        p = head
        
        i = 0
        while i < (len // 2):
            i += 1
            p = p.next
        
        while p:
            stack.append(p)
            p = p.next
        
        #----------------------
        # MAIN LOGIC
        p1 = head
        while stack:
            p2 = stack.pop()
            if p1 == p2:
                p1.next = None
                break
            temp = p1.next
            p1.next = p2
            if p2 == temp:
                p2.next = None
                break
            p2.next = temp
            p1 = temp