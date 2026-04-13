# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        one, two = list1, list2
        dummy = ListNode(val=0, next=None)
        current = dummy
        while one and two:
            if one.val < two.val:
                current.next = one
                one = one.next
            else:
                current.next = two
                two = two.next
            current = current.next
        if one:
            current.next = one
        if two:
            current.next = two
        return dummy.next



