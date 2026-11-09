# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            if list1: return list1
            if list2: return list2
            return None

        head = ListNode()
        head_copy = head
        head_ccopy = head_copy

        while list1 and list2:
            if list1.val <= list2.val:
                head.val = list1.val
                list1 = list1.next
            else:
                head.val = list2.val
                list2 = list2.next
            head.next = ListNode(404)
            head = head.next
        while list1:
            head.val = list1.val
            list1 = list1.next
            head.next = ListNode(404)
            head = head.next
        while list2:
            head.val = list2.val
            list2 = list2.next
            head.next = ListNode(404)
            head = head.next
        while head_copy.next.val != 404:
            head_copy = head_copy.next
        head_copy.next = None
        return head_ccopy

        




        