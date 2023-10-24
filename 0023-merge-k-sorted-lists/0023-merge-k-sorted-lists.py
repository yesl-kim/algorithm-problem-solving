# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        p = head = ListNode()
        while any(lists):
            i = smallest = None
            for j, node in enumerate(lists):
                if not node:
                    continue
                if not smallest or (smallest and smallest.val > node.val):
                    i, smallest = j, node
            lists[i] = smallest.next
            p.next, smallest.next = smallest, None
            p = p.next
        return head.next