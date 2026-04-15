# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while True:
            min_node = None
            for i, node in enumerate(lists):
                if not node:
                    continue
                if min_node is None or lists[min_node].val > lists[i].val:
                    min_node = i
            if min_node is None:
                break
            current.next = lists[min_node]
            lists[min_node] = lists[min_node].next
            current = current.next

        return dummy.next


