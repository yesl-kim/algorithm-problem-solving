# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pop(self, node):
        prev = None
        while node.next:
            prev = node
            node = node.next
        if prev:
            prev.next = None
        return node
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node = head
        while node:
            next = node.next
            last = self.pop(node)
            if node == next:
                return
            node.next = last
            if next == last:
                return
            last.next= next
            node = next